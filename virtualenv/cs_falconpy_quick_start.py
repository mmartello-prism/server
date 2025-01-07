"""CrowdStrike FalconPy Quick Start."""
import os
from dotenv import load_dotenv
from falconpy import Hosts
from art import text2art

# Load env variables
load_dotenv()

# Use the API Clients and Keys page within your Falcon console to generate credentials.
# You will need to assign the Hosts: READ scope to your client to run this example.

# CrowdStrike does not recommend you hardcode credentials within source code.
# Instead, provide these values as variables that are retrieved from the environment,
# read from an encrypted file or secrets store, provided at runtime, etc.

hosts = Hosts(client_id=os.getenv("FALCON_CLIENT_ID"), client_secret=os.getenv("FALCON_CLIENT_SECRET"))

# While this example retrieves credentials from the environment as the variables
# "FALCON_CLIENT_ID" and "FALCON_CLIENT_SECRET". Developers leveraging environment
# authentication do not need to specify the client_id or client_secret keywords.
#
# hosts = Hosts()

def __search_Hosts(host):
    # SEARCH_FILTER = "hostname-search-string"
    SEARCH_FILTER = 'SEC-ENG-CBO'

    # Retrieve a list of hosts that have a hostname that matches our search filter
    hosts_search_result = host.query_devices_by_filter(filter=f"hostname:*'*{SEARCH_FILTER}*'")

    # Confirm we received a success response back from the CrowdStrike API
    if hosts_search_result["status_code"] == 200:
        hosts_found = hosts_search_result["body"]["resources"]
        # Confirm our search produced results
        if hosts_found:
            # Retrieve the details for all matches
            hosts_detail = host.get_device_details(ids=hosts_found)["body"]["resources"]
            return hosts_detail
            # for detail in hosts_detail:
            #     # Display the AID and hostname and more for this match
            #     aid = detail["device_id"]
            #     hostname = detail["hostname"]
            #     print(f"\nHostname: {hostname}\naid: ({aid})")
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

# Recursion Method to travse unknonwn depth of JSON object
def __recursive_Object(data, indent=int(0)):
    # Dictionary check
    if isinstance(data, dict):
        for key, value in data.items():
            print(" " * indent + str(key) + ":")
            __recursive_Object(value, indent + 2)
    # List check
    elif isinstance(data, list):
        for item in data:
            __recursive_Object(item, indent)
    else:
        print(" " * indent + str(data))

# Main Method
def main():
    print(text2art("Falcon API", font="small"))
    print("Searching......\n")
    output = __recursive_Object(__search_Hosts(hosts), 0)
    # output = __search_Hosts(hosts)
    return output

if __name__ == '__main__':
    main()