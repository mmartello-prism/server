'''
#
# Filename: geNetworkMerakiAuthUsers.py
#
# Author: Mike Martello
# Date: 4/4/2024
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
NETWORK_ID = 'L_744782788376407195' # input network id
URI = 'merakiAuthUsers'

# HTTP Request from Meraki
# in this case, we use a GET request to fetch the syslog server 
# configuration data.
def __get_Syslog_Server(apikey):
    
    url = f"https://api.meraki.com/api/v1/networks/{str(NETWORK_ID)}/{str(URI)}"

    payload = None

    headers = {
        "Authorization": "Bearer " + apikey,
        "Accept": "application/json"
    }

    # Try/catch block to fetch syslog server config info
    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        response.raise_for_status() # Raise exception for HTTP errors
        results = response.json() # Return results of response
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching organization networks:\n{e}")
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
    print("\nList Meraki Auth Users:")
    print("----------------------------------")
    syslog = __recursive_object_traversal(__get_Syslog_Server(API_KEY), 0)
    return syslog

if __name__ == '__main__':
    main()