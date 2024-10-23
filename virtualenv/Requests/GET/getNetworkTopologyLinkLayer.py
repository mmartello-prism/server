'''
# Filename: getNetworkTopologyLinkLayer.py
# Author: Mike Martello
# Date: 7/12/2024
# Version: 1.0.0
#
'''
import os
import requests
from dotenv import load_dotenv
from art import text2art

# Load env variables
load_dotenv()

# Define Meraki API base URL
MERAKI_BASE_URL = 'https://api.meraki.com/api/v1'
# Meraki & Envrionment variables
API_KEY = os.getenv('MERAKI_KEY')
# NETWORK_ID 
NETWORK_ID = "L_744782788376407269"

# HTTP Request from Meraki
# in this case, we use a GET request to fetch the syslog server 
# configuration data.
def __get_Syslog_Server(apikey):
    # system arg needs either networks or organizations
    url = f"{MERAKI_BASE_URL}/networks/{str(NETWORK_ID)}/appliance/ports"
    
    headers = {
        "Authorization": "Bearer " + str(apikey),
        "Accept": "application/json"
    }

    print(text2art("Meraki API", font="small"))
    # Try/catch block to fetch syslog server config info
    try:
        response = requests.get(str(url), headers=headers)
        # Conditional check for response type
        if response.status_code == 200 or response.ok == True:
            print(f"Response Success: {response.ok}\nResponse Code: {response.status_code}")
            print("----------------------------------\n")
            results = response.json() # Return results of response
            return results
        else: 
            print(f"Response Success: {response.ok}\nResponse Code: {response.status_code}")
            results = response.text # Return results of response
            return results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching syslog server config info:\n{e}")
        return None

# Recursion Method to travse unknonwn depth of JSON object
def __recursive_object_traversal(data, indent=int(0)):
    # Dictionary check
    if isinstance(data, dict):
        for key, value in data.items():
            print(" " * indent + str(key) + ":")
            __recursive_object_traversal(value, indent + 2)
    # List check
    elif isinstance(data, list):
        for item in data:
            __recursive_object_traversal(item, indent)
    else:
        print(" " * indent + str(data))
        
# Main Method to execute script
def main():
    syslogServer = __recursive_object_traversal(__get_Syslog_Server(API_KEY), 0)
    return syslogServer

if __name__ == '__main__':
    main()