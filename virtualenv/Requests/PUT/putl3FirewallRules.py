'''
#
# Filename: putl3FirewallsRules.py
#
# Authored by: Mike Martello
# Date: 3/20/2024
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
NETWORK_ID = "L_744782788376407223"
# Appliance type
LAYER_3 = 'l3FirewallRules'

# Update MX firewall rules
def __update_MX_Firewall_Rules(apikey):

    url = f'{str(MERAKI_BASE_URL)}/networks/{str(NETWORK_ID)}/appliance/firewall/{str(LAYER_3)}'

    json_dict = {
        "rules": [
            {
                "comment": "Deny File Transfer Protocol (FTP) Traffic",
                "policy": "deny",
                "protocol": "ftp",
                "destPort": "20",
                "destCidr": "192.168.1.0/24",
                "srcPort": "Any",
                "srcCidr": "Any",
                "syslogEnabled": False
            }
        ]
    }
    
    # Needed to convert json object to multi-line string
    payload = json.dumps(json_dict)
    
    headers = {
        'Authorization': 'Bearer ' + str(apikey),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Try/Catch block for adding firewall rules
    try:
        response = requests.put(url, headers=headers, data=payload)
        if response.status_code == 200:
            print("Update successful!\n")
            print(f'Response: {response.json()}\n')
        else:
            print(f'Update failed with status code: {response.status_code}')
            print(f'Response: {response.text.encode('utf8')}')
    except requests.exceptions.RequestException as e:
        print(f'Error requesting L3 Firewall Rules info:\n{e}')
        return None

# Main Method
def main():
    print(text2art("Meraki API", font="small"))
    print("Updating L3 Firewall Rules.....\n")
    __update_MX_Firewall_Rules(API_KEY)

if __name__ == '__main__':
    main()