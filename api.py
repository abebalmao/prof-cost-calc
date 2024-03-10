import requests

from util.config import Config

config = Config()


def fetch_auction_data():
    access_token = open("secrets/access_token.txt", "r").readline()
    headers = { "Authorization": f"Bearer {access_token}", }


    response = requests.get(config.api__endpoint_eu_sod_crusader_strike_horde, headers=headers)
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"GET request failed with status code {response.status_code}")
        print("Error message:")
        print(response.text)
        
        exit(0) # Exit program

    print("GET request successful, writing to file: util/out/auctions_raw.json")


    file = open(config.file_path__output_api_auctions_raw, "w")

    file.write(response.text)