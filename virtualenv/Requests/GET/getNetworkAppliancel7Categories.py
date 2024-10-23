'''
#
# Filename: getNetworkAppliancel7Categories.py
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
NETWORK_ID = "L_744782788376407306"
# Appliance type
LAYER_7 = 'l7FirewallRules'

# Update MX firewall rules
def __update_MX_Firewall_Rules(apikey):

    url = f"{MERAKI_BASE_URL}/networks/{str(NETWORK_ID)}/appliance/firewall/l7FirewallRules/applicationCategories"
    
    headers = {
        'Authorization': 'Bearer ' + str(apikey),
        'Accept': 'application/json'
    }

    # Try/Catch block for adding firewall rules
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Request successfull!\n")
            print(f'Response: {response.json()}\n')
        else:
            print(f'Request failed with status code: {response.status_code}')
            print(f'Response: {response.text.encode('utf8')}')
    except requests.exceptions.RequestException as e:
        print(f'Error requesting L7 Firewall Rules info:\n{e}')
        return None

# Main Method
def main():
    print(text2art("Meraki API", font="small"))
    print("Requesting L7 Firewall Rules.....\n")
    __update_MX_Firewall_Rules(API_KEY)

if __name__ == '__main__':
    main()