'''
#
# Filename: getOrganizations.py
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

# Env variables
API_KEY = os.getenv('MERAKI_KEY')

# Get Meraki Organization List
def __get_Meraki_Organizations(api_key):
    
    # Request parameters for fetching organizations
    url = 'https://api.meraki.com/api/v1/organizations'
    payload = None
    headers = {
        'Authorization': 'Bearer ' + str(api_key),
        'Accept': 'application/json'
    }

    # Try/Catch block to fetch organiztion list
    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        response.raise_for_status() # Raise exception for HTTP errors
        org_data = response.json() # Return results of response
        return org_data
    except requests.exceptions.RequestException as e:
        print('Error fetching organizations:', e)
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
    organizations =  __recursive_object_traversal(__get_Meraki_Organizations(API_KEY), 0)
    return organizations

if __name__ == "__main__":
    main()