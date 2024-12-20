"""CrowdStrike FalconPy Quick Start."""
import os
from dotenv import load_dotenv
from falconpy import Hosts

# Load env variables
load_dotenv()

# Use the API Clients and Keys page within your Falcon console to generate credentials.
# You will need to assign the Hosts: READ scope to your client to run this example.

# CrowdStrike does not recommend you hardcode credentials within source code.
# Instead, provide these values as variables that are retrieved from the environment,
# read from an encrypted file or secrets store, provided at runtime, etc.

hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"), 
              client_secret=os.getenv("FALCON_CLIENT_SECRET"))

# While this example retrieves credentials from the environment as the variables
# "FALCON_CLIENT_ID" and "FALCON_CLIENT_SECRET". Developers leveraging environment
# authentication do not need to specify the client_id or client_secret keywords.
#
# hosts = Hosts()

# SEARCH_FILTER = "hostname-search-string"
SEARCH_FILTER = 'revenue-cbo-0092'

# Retrieve a list of hosts that have a hostname that matches our search filter
hosts_search_result = hosts.query_devices_by_filter(filter=f"hostname:*'*{SEARCH_FILTER}*'")

# Confirm we received a success response back from the CrowdStrike API
if hosts_search_result["status_code"] == 200:
    hosts_found = hosts_search_result["body"]["resources"]
    # Confirm our search produced results
    if hosts_found:
        # Retrieve the details for all matches
        hosts_detail = hosts.get_device_details(ids=hosts_found)["body"]["resources"]
        print(hosts_detail)
        for detail in hosts_detail:
            # Display the AID and hostname for this match
            aid = detail["device_id"]
            hostname = detail["hostname"]
            status = detail["status"]
            mac_address = detail["mac_address"]
            first_seen = detail["first_seen"]
            connection_ip = detail["connection_ip"]
            chassis_type_desc = detail["chassis_type_desc"]
            system_manufacturer = detail["system_manufacturer"]
            os_product_name = detail["os_product_name"]

            print(f"\nHostname: {hostname}\naid: ({aid})\nStatus: {status}\nMac Address: {mac_address}\nFirst Seen: {first_seen}\nConnection IP: {connection_ip}\nChassis Type: {chassis_type_desc}\nSystem Manufacturer: {system_manufacturer}\nOperating Sytem: {os_product_name}\n")
    else:
        print("No hosts found matching that hostname within your Falcon tenant.")
else:
    # Retrieve the details of the error response
    error_detail = hosts_search_result["body"]["errors"]
    for error in error_detail:
        # Display the API error detail
        error_code = error["code"]
        error_message = error["message"]
        print(f"[Error {error_code}] {error_message}")