'''
#
# Filename: getNetworkTags.py
#
# Author: Mike Martello
# Date: 4/1/2024
# Version: 1.0.0
#
'''
import os
import requests
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Meraki & Envrionment variables
API_KEY = os.getenv('MERAKI_KEY')
NETWORK_ID = 'L_744782788376407178' # input network id

# GET Request for network tags
def getNetworkTags(apikey):
    url = f'https://api.meraki.com/api/v1/networks/{str(NETWORK_ID)}'

    payload = None

    headers = {
        "Authorization": "Bearer " + str(apikey),
        "Accept": "application/json"
    }

    # Try/Catch block to fetch network tags
    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        response.raise_for_status() # Raise exception for HTTP errors
        networks = response.json() # Return results of response
        return networks
    except requests.exceptions.RequestException as e:
        print(f"Error fetching network tags:\n{e}")
        return None

# Main Method to execute script
def main():
    net_tags = getNetworkTags(API_KEY)
    if net_tags:
        print('\nList of Network Tags:')
        print('---------------------')
        for i, tags in enumerate(net_tags['tags']):
            print(f"Tag {i}: {tags}")
        print('---------------------')
            
if __name__ == '__main__':
    main()