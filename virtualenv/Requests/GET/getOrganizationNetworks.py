'''
#
# Filename: getOrganizationNetworks.py
#
# Authored by: Mike Martello
# Date: 3/20/2024
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
ORG_ID = os.getenv('ORG_ID')
URI = 'networks'

# HTTP Request from Meraki
# in this case, we use a GET request to fetch the 
# organization's networks configuration data.
def __get_Organization_Networks(apikey):

    url = f"https://api.meraki.com/api/v1/organizations/{str(ORG_ID)}/{str(URI)}"

    headers = {
        "Authorization": "Bearer " + str(apikey),
        "Accept": "application/json"
    }

    # Try/Catch block to fetch organization networks
    try:
        response = requests.request('GET', url, headers=headers)
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

# Main Method
def main():
    print("\nList of Networks")
    print("----------------------------------")
    # networks = __recursive_object_traversal(__get_Organization_Networks(API_KEY), 0)
    networks = __get_Organization_Networks(API_KEY)
    return networks

if __name__ == "__main__":
    main()
