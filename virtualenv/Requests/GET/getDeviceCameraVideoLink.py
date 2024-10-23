'''
#
# Filename: getDeviceCameraVideoLink.py
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
URI = 'camera/videoLink'
SERIAL = "" # Need to locate/find a serial id to view video feed

def __get_Device_Camera_Video_Link(apikey, serial):
    url = f"https://api.meraki.com/api/v1/devices/{serial}/{str(URI)}"

    payload = None

    headers = {
        "Authorization": "Bearer " + apikey,
        "Accept": "application/json"
    }

    # Try/Catch Block for Camera feed
    try:
        response = requests.request('GET', url, headers=headers, data = payload)
        response.raise_for_status()
        device_camera = response.json()
        return device_camera
    except requests.exceptions.RequestException as e:
        print('Error fetching device camera feed:', e)
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
    camera = __recursive_object_traversal(__get_Device_Camera_Video_Link(API_KEY), 0)
    return camera

if __name__ == "__main__":
    main()