import json
import os
import shutil
import sqlite3
import csv
import pandas as pd
from datetime import datetime

from util.config import Config

config = Config()

conn = sqlite3.connect(config.db__file_path)
crsr = conn.cursor()



def get_data_age(table_name, tb_timestamp_col="dev_ingested_at"):
    # return values: days, hours, minutes

    tb_row_count = crsr.execute(f"select count(1) from {table_name}"
                                ).fetchone()[0]

    if tb_row_count != 0:
        tb_last_row_update = crsr.execute(f"select max({tb_timestamp_col}) from {table_name} order by {tb_timestamp_col} limit 1").fetchone()[0]
        
        current_time = datetime.now()
        timestamp_from_db = datetime.strptime(tb_last_row_update, '%Y-%m-%d %H:%M:%S')
        diff = current_time - timestamp_from_db

        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        data_age_in_minutes = (days * 1440) + (hours * 60) + minutes

        return days, hours, minutes, data_age_in_minutes
    
    else: 
        return 0, 0, 0, 0



def init_lkp_tables():

    # items_lkp
    crsr.execute(f"drop table if exists {config.tb_name__lkp_items};"); conn.commit()
    schema_items_lkp = f"""
        create table {config.tb_name__lkp_items} (
            _item_id integer,
            item_name text,
            dev_ingested_at datetime
        );
    """
    crsr.execute(schema_items_lkp);conn.commit()


    # professions_lkp
    crsr.execute(f"drop table if exists {config.tb_name__lkp_professions};"); conn.commit()
    schema_professions_lkp = f"""
        create table {config.tb_name__lkp_professions} (
           _profession_id integer,
           profession_name text,
           dev_ingested_at datetime
        );
    """
    crsr.execute(schema_professions_lkp);conn.commit()


    # recipe_definitions_lkp
    crsr.execute(f"drop table if exists {config.tb_name__lkp_recipe_definitions};"); conn.commit()
    schema_recipe_definitions_lkp = f"""
        create table {config.tb_name__lkp_recipe_definitions} (
            _craft_item_id integer,
            _reagent_item_id integer,
            reagent_quantity integer,
            reagent_is_created integer,         /* boolean */
            reagent_is_vendor_item integer,     /* boolean */
            reagent_profession_id,
            craft_profession_id,
            dev_ingested_at datetime
        );
    """
    crsr.execute(schema_recipe_definitions_lkp); conn.commit()


    # profession_leveling_routes_lkp
    crsr.execute(f"drop table if exists {config.tb_name__lkp_professions_leveling_routes};"); conn.commit()
    schema_profession_leveling_routes_lkp = f"""
        create table {config.tb_name__lkp_professions_leveling_routes} (
            _route_identifier text,
            _profession_id integer,
            _item_id integer,
            order_id integer,
            craft_quantity_guess integer,
            start_level integer,
            end_level integer,
            dev_ingested_at datetime
        );
    """
    crsr.execute(schema_profession_leveling_routes_lkp); conn.commit()



def init_raw_tables():

    # auctions
    schema_auctions = """
        create table if not exists auctions_raw (
            _id integer primary key autoincrement,
            _item_id integer,
            auction_house_id integer,
            min_buyout integer,
            quantity integer,
            market_value integer,
            historical integer,
            dev_ingested_at datetime
        );
    """

    crsr.execute(schema_auctions)
    conn.commit()



def lkp_table_need_update(table_name, file_path):
    tb_row_count = crsr.execute(f"select count(1) from {table_name};"
                                ).fetchone()[0]

    with open(file_path, "r") as file: 
        csv_reader = csv.reader(file)
        file_row_count = sum(1 for row in csv_reader)

    # See if there is an update in the file, (-1 is the header)
    # if there is no update, return
    if tb_row_count == (file_row_count - 1):
        return False
    
    return True



def maintain_professions_lkp():
    table_name="professions_lkp"
    file_path=config.file_path__lkp_professions

    if lkp_table_need_update(table_name, file_path):

        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            insert_query = f"insert into {table_name} values(?, ?, datetime('now', 'localtime'))"
            data = [tuple(row) for row in csv_reader]
            crsr.executemany(insert_query, data)

        conn.commit()



def maintain_items_lkp():
    table_name="items_lkp"
    file_path=config.file_path__lkp_items

    if lkp_table_need_update(table_name, file_path):
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            insert_query = f"insert into {table_name} values(?, ?, datetime('now', 'localtime'))"
            data = [tuple(row) for row in csv_reader]
            crsr.executemany(insert_query, data)

        conn.commit()



def maintain_recipe_definitions_lkp():
    table_name="recipe_definitions_lkp"
    file_path=config.file_path__lkp_recipe_definitions

    if lkp_table_need_update(table_name, file_path):
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            insert_query = f"insert into {table_name} values(?, ?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))"
            data = [tuple(row) for row in csv_reader]
            crsr.executemany(insert_query, data)

        conn.commit()



def maintain_profession_leveling_routes_lkp():
    table_name = config.tb_name__lkp_professions_leveling_routes
    dir_path = config.dir_path__lkp_professions_leveling_routes

    for file in os.listdir(dir_path):

        file_path = dir_path + file

        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            insert_query = f"insert into {table_name} values(?, ?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))"
            data = [tuple(row) for row in csv_reader]
            crsr.executemany(insert_query, data)

        conn.commit()



def load_auction_data():

    try:
        with open('util/out/auctions_raw.json', 'r') as file:
            data = json.load(file)

        timestamp = crsr.execute("select datetime('now', 'localtime')").fetchone()[0]

        for record in data:

            auction_house_id = record['auctionHouseId']
            item_id = record['itemId']
            min_buyout = record['minBuyout']
            quantity = record['quantity']
            market_value = record['marketValue']
            historical = record['historical']


            query = """
                insert into auctions_raw (
                    _item_id, auction_house_id, min_buyout, quantity, market_value, historical, dev_ingested_at
                ) values (
                    ?, ?, ?, ?, ?, ?, ?
                )
            """
            crsr.execute(query, (item_id, auction_house_id, min_buyout, quantity, market_value, historical, timestamp))
            conn.commit()

        print('Rows ingested: ' + 
            str(crsr.execute("""
                select count(1) 
                from auctions_raw 
                where dev_ingested_at='{}'
                """.format(timestamp)
                ).fetchone()[0]))
        
        # Move file to archive and set timestamp in name

        parsed_timestamp = timestamp[:10]

        if os.path.exists(f"util/out/archive/{parsed_timestamp}/") == False:
            os.makedirs(f"util/out/archive/{parsed_timestamp}/")

        shutil.move("util/out/auctions_raw.json", 
                    f"util/out/archive/{parsed_timestamp}/auctions_raw.json")
        print(f"moved file auction_raw.json to archive with timestamp: {parsed_timestamp}")
    
    except FileNotFoundError:
        print(f"Did not find the file auctions_raw.json. Did you fetch the new data?")

    except Exception as e:
        print(f"unexpected exception {e}")



# game loop
def maintain_lkp_tables():
    
    init_lkp_tables()

    maintain_professions_lkp()
    maintain_items_lkp()
    maintain_recipe_definitions_lkp()
    maintain_profession_leveling_routes_lkp()
