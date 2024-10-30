'''
#
# Filename: putl7FirewallsRules.py
#
# Authored by: Mike Martello
# Date: 3/20/2024
# Version: 1.1.0
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
NETWORK_ID = 'L_744782788376407230'

# Update MX firewall rules
def __update_MX_Firewall_Rules(apikey):

    url = f'{MERAKI_BASE_URL}/networks/{NETWORK_ID}/appliance/firewall/l7FirewallRules'

    json_dict = {
        "rules": [
            {"policy":"deny", "type": "ipRange", "value": "157.254.165.47/32"},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/106", "name": "Apple file sharing"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/9", "name": "Dropbox"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/171", "name": "Box"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/38", "name": "Netflix"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/2687", "name": "Disney"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/36", "name": "hulu.com"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/178", "name": "HBO GO"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/1892", "name": "Sling"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/2294", "name": "TikTok"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/4", "name": "Gmail"}},
            {"policy":"deny", "type": "application", "value": {"id": "meraki:layer7/application/130", "name": "Yahoo Mail"}}
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
        print(f'Error Requesting L7 Firewall Rules info:\n{e}')
        return None

# Main Method
def main():
    print(text2art("Meraki API", font="small"))
    print("Updating L7 Firewall Rules.....\n")
    __update_MX_Firewall_Rules(API_KEY)

if __name__ == '__main__':
    main()