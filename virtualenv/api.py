'''
#
# Filename: Flask App for Security Workbench
# Author: Mike Martello
# Version: 2.2.0
#
'''
import os
import requests
import time
from dotenv import load_dotenv
from flask import Flask
from markupsafe import escape
import base64

# Load env variables
load_dotenv()

# Get Meraki API Key
API_KEY = os.getenv('MERAKI_KEY')
# Define Meraki API base URL
MERAKI_BASE_URL = os.getenv('MERAKI_BASE_URL')
# CrowdStrike API
CS_CLIENT_ID = os.getenv('FALCON_CLIENT_ID')
CS_CLIENT_SECRET = os.getenv('FALCON_CLIENT_SECRET')
CS_BASE_URL = os.getenv('FALCON_CLIENT_BASE_URL')

# Combine client_id and client secret
credentials = f"{CS_CLIENT_ID}:{CS_CLIENT_SECRET}"

# Envoke the credentials
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

# Initialize Flask
app = Flask(__name__)

# Networks
@app.route('/networks/<string:network_id>/<path:subpath>')
def request_networks_meraki(network_id, subpath):
    # system arg needs either networks or organizations
    url = f"{str(MERAKI_BASE_URL)}/networks/{network_id}/{escape(subpath)}"
        
    headers = {
        "Authorization": "Bearer " + str(API_KEY),
        "Accept": "application/json"
    }

    # Try/catch block to fetch config info
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

    # Try/catch block to fetch config info
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

#CrowdStrike Total Device Count
@app.route('/falcon-complete-dashboards/<path:subpath>')
def request_total_device_count(subpath):
    url = f"{CS_BASE_URL}/falcon-complete-dashboards/{escape(subpath)}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    print('/aggregates/total-device-counts/v1')

    # Try/catch block to fetch config info
    try:
        response = response.get(str(url), headers=headers)
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