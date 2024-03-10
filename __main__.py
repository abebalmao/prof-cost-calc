
from tabulate import tabulate

from util.config import Config
from db import get_data_age, load_auction_data, maintain_lkp_tables
from api import fetch_auction_data

config = Config()

# globals for fetching more data
global auctions_raw_fetch_more; auctions_raw_fetch_more = False

def maintain_auctions_raw():

    table_name = config.data_auctions__tb_name
    data_age_limit_minutes = int(config.data_auctions__cutoff)
    fetch_more = False
    days, hours, minutes, data_age_in_minutes = get_data_age(table_name)

    if data_age_in_minutes > data_age_limit_minutes:
        fetch_more = True

    return f"{days}d {hours}h {minutes}m", fetch_more

def fetch_more_data():
    
    if auctions_raw_fetch_more:
        print(f"Fetching more data for table 'auctions_raw'")
        fetch_auction_data()
        load_auction_data()   


def print_commands():
    
    print("  'fetch' - fetches more data to those with old data")
    print("  'query' - enters query mode")
    print("  'refresh' - reloads the lookup tables")
    print("  'exit' - exit script")


def user_input_switch(string):

    if string == "fetch" or string == "f":
        fetch_more_data()

    elif string == "help" or string == "h":
        print_commands()

    elif string == "query" or string == "q":
        print("entering query mode...")

    elif string == "refresh" or string == "r":
        maintain_lkp_tables()

    elif string == "exit" or string == "e":
        exit(0)
    else:
        print(f"'{string}' not a valid command, type 'help' or 'h' for a list of commands")


def main():
    
    # Get time for all tables
    auctions_raw_time, auctions_raw_fetch_more = maintain_auctions_raw()
    globals().update(auctions_raw_fetch_more=auctions_raw_fetch_more)


    table = [
        ['table_name', 'time_since_last_ingestion', 'cutoff', 'eligible_for_fetch'],
        [config.data_auctions__tb_name, auctions_raw_time, config.data_auctions__cutoff + ' ' + config.data_auctions__cutoff_type, auctions_raw_fetch_more]
    ]

    print(f"0== {config.script_version} ==========================================================0")
    print(tabulate(table, headers='firstrow'))
    
    while(True):
        user_input = input("> ")
        user_input_switch(user_input)


main()