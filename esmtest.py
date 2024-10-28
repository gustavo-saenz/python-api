"""Example script for ArcSight community

Example script to communicate and fetch an event in ArcSight ESM
"""
import json
import argparse
from collections import OrderedDict
from dataclasses import replace
from pickle import FALSE

import requests


def parse_command_line():
    """Stores the values passed by the user when running the script"""
    parser = argparse.ArgumentParser(description='Script to convert subnets to full descriptive ranges')
    parser.add_argument('--username', required=False, help='ESM Username', default='admin')
    parser.add_argument('--password', required=False, help='ESM Password', default='arcsight')
    parser.add_argument('--host', required=False, help='IP or hostname of ESM', default='esm.test.lab')
    parser.add_argument('--port', required=False, help='Port to use for the requests', default='8443')
    parser.add_argument('--eventid', required=False, help='An existing EventID on ESM', default='786013')
    parser.add_argument('--verifyssl', required=False, help='Verify SSL Certificate or not', default=False)

    args = parser.parse_args()

    return args

def api_request(url, data, requesttype, verifyssl):
    """Prepares all API requests

    Best to have one function handle all requests,
    in that way we can ensure all requests have the same
    way of catching both errors and formating responses.

    Arguments:
        url {string} -- Full url of the API call.
        data {array} -- An array of parameters, either sent as JSON or urlparams.
        requesttype {string} -- Either GET or POST.
        verifyssl {string} -- If we are verifying the SSL certificate or not.

    Returns:
        string -- Response of the API request in json format, no error control yet.
    """
    if not data:
        return "No input was given"

    headers = ({'Accept' : 'application/json', 'Content-Type': 'application/json'})

    if requesttype.lower() == "post":
        response = requests.post(url, json=data, verify=verifyssl, headers=headers)
        return response.json()

    #Todo: Add get, not enough time to finish
    return requests.get(url, data, verify=verifyssl, headers=headers)


def login(args):
    """Logs the user in

    Logs the user in with the supplied username and password, and returns a token

    Arguments:
        username {string} -- Username of the ESM API user
        password {string} -- Password of the ESM API user

    Returns:
        string -- Userid if the authentication is successful
    """
    url = "https://" +  args.host  + ":" +  args.port  + "/www/core-service/rest/LoginService/login"
    data = {
        "log.login" : {
            "log.login" : args.username,
            "log.password" : args.password
        }
    }
    response = api_request(url, data, 'post', args.verifyssl)

    return response["log.loginResponse"]["log.return"]


def get_event(args, authtoken):
    """Returns detailed information about events

    Expects minimum one ID, or an array, then returns details about each ID

    Arguments:
        args {array} -- Array of arguments supplied from the commandline
        authtoken {string} -- The authentication token of the user

    Returns:
        array -- Returns an array of results, depending on how many id's was requested
    """
    url = "https://" +  args.host  + ":" +  args.port  + "/www/manager-service/rest/SecurityEventService/getSecurityEvents"
    data = {
        "sev.getSecurityEvents" : {
            "sev.authToken" : authtoken,
            "sev.ids" : args.eventid,
            "sev.startMillis" : "-1",
            "sev.endMillis" : "-1"
        }
    }
    return api_request(url, data, 'post', args.verifyssl)


def main():
    """Lazy main to get rid of linting errors

    Some random docs
    """
    args = parse_command_line()
    authtoken = login(args)
    event_details = get_event(args, authtoken)

    try:
        print("This is the token: " + authtoken)
        print(event_details)
        print(event_details["sev.getSecurityEventsResponse"]["sev.return"]["concentratorAgents"]["zone"]["referenceString"])
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    main()

# this script needs to be run like this: python test.py --username someuser --password "somepassword" --host 192.168.1.1 --eventid 6565274