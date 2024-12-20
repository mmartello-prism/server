'''
#
# Filename: getl7FirewallRules.py
#
# Author: Mike Martello
# Date: 12/17/2024
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
NETWORK_ID = 'L_744782788376407570' # input network id

# GET Request for firewall services
def __get_Firewall_Rules(apikey):

    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/appliance/firewall/l7FirewallRules"

    payload = None

    headers = {
        "Authorization": "Bearer " + str(apikey),
        "Accept": "application/json"
    }

    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        response.raise_for_status() # Raise exception for HTTP errors
        results = response.json() # Return results of response
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching l7 Firewall Rules:\n{e}")
        return None
    
# Recursion Method to travse unknonwn depth of JSON object
def __recursive_object_traversal(data, indent=int(0)):
    if isinstance(data, dict):
        for key, value in data.items():
            print(" " * indent + str(key) + ":")
            __recursive_object_traversal(value, indent + 2)
    elif isinstance(data, list):
        for item in data:
            __recursive_object_traversal(item, indent)
    else:
        print(" " * indent + str(data))

# Main Method to execute script
def main():
    fwRules = __recursive_object_traversal(__get_Firewall_Rules(API_KEY), 0)
    return fwRules

if __name__ == "__main__":
    main()