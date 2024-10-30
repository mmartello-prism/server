'''
#
# Filename: putContentFiltering.py
#
# Authored by: Mike Martello
# Date: 9/23/2024
# Version: 1.0.0
#
'''
import os
import requests
import json
from art import text2art
from dotenv import load_dotenv

# Load env variables
load_dotenv()
# Define Meraki API base URL
MERAKI_BASE_URL = 'https://api.meraki.com/api/v1'
# Meraki & Envrionment variables
API_KEY = os.getenv('MERAKI_KEY')
# Location network id
NETWORK_ID = "L_744782788376402478"

# Update MX firewall rules
def __update_Content_Filtering(apikey):

    url = f'{MERAKI_BASE_URL}/networks/{NETWORK_ID}/appliance/contentFiltering'

    json_dict = {
        "allowedUrlPatterns": [
            "https://intellechart.net"
        ],
        "blockedUrlPatterns": [
            "drive.google.com",
            "icloud.com",
            "dropbox.com",
            "box.com",
            "netflix.com",
            "disneyplus.com",
            "sling.com",
            "max.com",
            "hulu.com",
            "tiktok.com"
        ],
        "blockedUrlCategories": [
            "meraki:contentFiltering/category/C6",
            "meraki:contentFiltering/category/C119",
            "meraki:contentFiltering/category/C109",
            "meraki:contentFiltering/category/C84",
            "meraki:contentFiltering/category/C78",
            "meraki:contentFiltering/category/C77",
            "meraki:contentFiltering/category/C75",
            "meraki:contentFiltering/category/C64",
            "meraki:contentFiltering/category/C60",
            "meraki:contentFiltering/category/C54",
            "meraki:contentFiltering/category/C51",
            "meraki:contentFiltering/category/C50",
            "meraki:contentFiltering/category/C49",
            "meraki:contentFiltering/category/C47",
            "meraki:contentFiltering/category/C36",
            "meraki:contentFiltering/category/C34",
            "meraki:contentFiltering/category/C36",
            "meraki:contentFiltering/category/C36",
            "meraki:contentFiltering/category/C36"
        ]
    }

    # Needed to convert json object to multi-line string
    payload = json.dumps(json_dict)
    
    headers = {
        'Authorization': 'Bearer ' + str(apikey),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Try/Catch block for adding Firewall Rules
    try:
        response = requests.put(str(url), headers=headers, data=payload)
        # Conditional check for response type
        if response.status_code == 200 or response.ok == True:
            print(f"Response Success: {response.ok}\nResponse Code: {response.status_code}")
            print("----------------------")
            print(f"Updated Network ID: {NETWORK_ID}\n")
            results = response.json() # Return results of response
            return results
        else:
            print(f"Response Success: {response.ok}\nResponse Code: {response.status_code}")
            print(f'Response: {response.text.encode('utf8')}')
            results = response.text # Return results of response
            return results
    except requests.exceptions.RequestException as e:
        print(f'Error requesting Content Filtering info:\n{e}')
        return None

# Main Method
def main():
    print(text2art("Meraki API", font="small"))
    print("Updating Content Filtering.....\n")
    __update_Content_Filtering(API_KEY)

if __name__ == '__main__':
    main()