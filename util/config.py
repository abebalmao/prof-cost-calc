class Config():

    def __init__(self):

        self.script_version = "v0.1.0"
        self.config_verison = "v0.1.0"

        # settings
        self.log_to_file = 1

        # db
        self.db__name = "dev.db"
        self.db__file_path = "util/db/dev.db"
        self.file_path__lkp_realms = "util/lookup_tables/realms_lkp.csv"
        self.db__load_chunksize = 8000
        self.tb_name__phys_auctions_raw = "auctions_raw"
        
        # file insert
        self.delimiter = '|'

        # files
        self.file_path__tables_metadata = "util/_table_metadata.csv"

        # lkp tables
        self.tb_name__lkp_recipe_definitions = "recipe_definitions_lkp"
        self.file_path__lkp_recipe_definitions = "util/lookup_tables/recipe_definitions_lkp.csv"
        
        self.tb_name__lkp_professions_leveling_routes = "profession_leveling_routes_lkp"
        self.dir_path__lkp_professions_leveling_routes = "util/lookup_tables/profession_leveling_routes/"
        
        
        # api
        self.api__access_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJCVFIwUTVZMDZNeWxPUlRoUWRKb1hsYUdoYVJjcGtSVUpYZ3UzLUlvLXBZIn0.eyJleHAiOjE3MTA1OTYxNDAsImlhdCI6MTcwOTk5MTM0MCwianRpIjoiZTIyNTMyNjgtZjI3OS00NjRmLTliZWEtNjY4OTkwOTkxMDhkIiwiaXNzIjoiaHR0cHM6Ly9pZC50cmFkZXNraWxsbWFzdGVyLmNvbS9yZWFsbXMvYXBwIiwiYXVkIjpbImFwcC1kZXNrdG9wLWJhY2tlbmQiLCJhcHAtcmVhbG0iLCJhcHAtcHJpY2luZyIsImFjY291bnQiXSwic3ViIjoiZjoyZjliMjU1Yy1hZjlkLTQ5OTUtYmU0YS1jZjQyNjc3NzE4ZjA6MmI1MTVlMTEtYThiYi00YzZkLWJjY2MtY2ViY2ExOGE1ODU2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBpLWtleSIsInNlc3Npb25fc3RhdGUiOiI2ZTI5YjA1OS04ZWZhLTRmNjgtOWMyOC1iZGExM2ExNjBiY2EiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwibWVtYmVyIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhcHAtZGVza3RvcC1iYWNrZW5kIjp7InJvbGVzIjpbInJlYWxtcy9tYW5hZ2VyIl19LCJhcHAtcmVhbG0iOnsicm9sZXMiOlsiYXVjdGlvbi1ob3VzZXMvYWNjZXNzb3IiLCJyZWFsbXMvYWNjZXNzb3IiLCJyZWdpb25zL2FjY2Vzc29yIl19LCJhcHAtcHJpY2luZyI6eyJyb2xlcyI6WyJncmVhdC1kZWFscy9hY2Nlc3NvciIsImF1Y3Rpb24taG91c2UtcHJpY2VzL2FjY2Vzc29yIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJzaWQiOiI2ZTI5YjA1OS04ZWZhLTRmNjgtOWMyOC1iZGExM2ExNjBiY2EiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im5pZ2h0d2l0cyIsImVtYWlsIjoidHdpc3R5c3R1ZGlvc0BnbWFpbC5jb20ifQ.cQV07exp1REQo0MvZ5C6dPHGG23I5vURU_3VUbYEw1LmmpgOBgPFSIOvm9Jt3fK8KD1Ht9gAv-41TKL_ENaTrHe53366ZhrPKXumT-ugCKr4hiCLEAfk6xI2wQsqz1M-7H329lsH2TDRZ0f4g5XLVfeEzWOxpCJ1iSVAb1-f6mHfW11Ky6hGUifcYD6tLYb6Sb_T4kSnyW3QHtNha_LgkDDPx8afitphBpFizEzzh1WYVTffJJpCS5dVowPbzqmeVGs5Fv-bPKKdPVwVSTBNqvlYgV-6e5Y9ZmLLcySjdSGoOf84fTybRnrBeR5SJt3fxTISbgfRPU8pO0QUFFjtFA"
        self.api__endpoint_eu_sod_crusader_strike_horde = "https://pricing-api.tradeskillmaster.com/ah/516"
        self.api__realm_id_eu_sod_crusader_strike = "1070"
        self.api__ah_id_eu_sod_crusader_strike_horde = "516"
        
        self.file_path__output_api_auctions_raw = "util/out/auctions_raw.json"

        # auctions
        self.data_auctions__cutoff = '5'
        self.data_auctions__cutoff_type = 'minutes'
        self.data_auctions__tb_name = 'auctions_raw'
