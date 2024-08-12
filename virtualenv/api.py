'''
#
# Filename: Flask App for Security Workbench
# Author: Mike Martello
# Version: 2.1.1
#
'''
import os
import requests
import time
from dotenv import load_dotenv
from flask import Flask
from markupsafe import escape

# Load env variables
load_dotenv()

# Get Meraki API Key
API_KEY = os.getenv('MERAKI_KEY')
# Define Meraki API base URL
MERAKI_BASE_URL = os.getenv('MERAKI_BASE_URL')

# Initialize Flask
app = Flask(__name__)

# Networks
@app.route('/networks/<string:network_id>/<path:subpath>')
def request_networks_meraki(network_id, subpath):
    # system arg needs either networks or organizations
    if (subpath == 'traffic'):
        url = f"{str(MERAKI_BASE_URL)}/networks/{network_id}/traffic?timespan=86400"
    else:
        url = f"{str(MERAKI_BASE_URL)}/networks/{network_id}/{escape(subpath)}"
        
    headers = {
        "Authorization": "Bearer " + str(API_KEY),
        "Accept": "application/json"
    }

    # Try/catch block to fetch syslog server config info
    try:
        response = requests.get(str(url), headers=headers)
        # Conditional check for response type
        if response.status_code == 200:
            print("-----Returned Output:-----\n")
            results = response.json() # Return results of response
            return results
        elif response.status_code == 429:
            time.sleep(int(response.headers["Retry-After"]))
        else: 
            print(f"Response Code: {response.status_code}")
            results = response.text # Return results of response
            return results
    except requests.exceptions.RequestException as e:
        print(f"Expection Error fetching config info:\n{e}")
        return {'Error: ':e}

# Organization
@app.route('/organizations/<int:org_id>/<path:subpath>')
def request_organizations_meraki(org_id, subpath):
    # system arg needs either networks or organizations
    url = f"{str(MERAKI_BASE_URL)}/organizations/{org_id}/{escape(subpath)}"
    
    headers = {
        "Authorization": "Bearer " + str(API_KEY),
        "Accept": "application/json"
    }

    # Try/catch block to fetch syslog server config info
    try:
        response = requests.get(str(url), headers=headers)
        # Conditional check for response type
        if response.status_code == 200:
            print("-----Returned Output:-----\n")
            results = response.json() # Return results of response
            return results
        elif response.status_code == 429:
            time.sleep(int(response.headers["Retry-After"]))
        else: 
            print(f"Response Code: {response.status_code}")
            results = response.text # Return results of response
            return results
    except requests.exceptions.RequestException as e:
        print(f"Expection Error fetching config info:\n{e}")
        return {'Error: ':e}
