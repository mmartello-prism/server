'''
#
# Filename: putNetFlows.py
#
# Authored by: Mike Martello
# Date: 5/7/2024
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
NETWORK_ID = 'L_744782788376408372'

# Update MX firewall rules
def __update_SNMP(apikey):

    url = f'{str(MERAKI_BASE_URL)}/networks/{str(NETWORK_ID)}/snmp'

    json_dict = {
        "access": "community",
        "communityString": "MerakiSNMP"
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
        print(f'Error Requesting SNMP info:\n{e}')
        return None

# Main Method
def main():
    print(text2art("Meraki API", font="small"))
    print("Updating SNMP Settings.....\n")
    __update_SNMP(API_KEY)

if __name__ == '__main__':
    main()