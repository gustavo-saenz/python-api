import json
import argparse
import requests
import urllib3
import datetime
import time


def parse_command_line():
    """Stores the values passed by the user when running the script"""
    parser = argparse.ArgumentParser(description='Script to convert subnets to full descriptive ranges')
    parser.add_argument('--username', required=False, help='ESM Username', default='admin')
    parser.add_argument('--password', required=False, help='ESM Password', default='arcsight')
    parser.add_argument('--host', required=False, help='IP or hostname of ESM', default='esm.test.lab')
    parser.add_argument('--port', required=False, help='Port to use for the requests', default='8443')
    parser.add_argument('--eventid', required=False, help='An existing EventID on ESM', default="2161522, 2161523")
    parser.add_argument('--verifyssl', required=False, help='Verify SSL Certificate or not', default=False)

    args = parser.parse_args()

    return args



def login_api_call(url, data, requesttype, verifyssl):
    """Arguments:
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
    response = login_api_call(url, data, 'post', args.verifyssl)

    return response["log.loginResponse"]["log.return"]


def esm_api_call(url, data, requesttype, verifyssl, token):
    """Arguments:
        url {string} -- Full url of the API call.
        data {array} -- An array of parameters, either sent as JSON or urlparams.
        requesttype {string} -- Either GET or POST.
        verifyssl {string} -- If we are verifying the SSL certificate or not.

    Returns:
        string -- Response of the API request in json format, no error control yet.
    """
    if not data:
        return "No input was given"

    headers = {
        'accept' : 'application/json',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    if requesttype.lower() == "post":
        eventjson = requests.post(url, json=data, verify=verifyssl, headers=headers)
    else:
        eventjson = requests.get(url, data, verify=verifyssl, headers=headers)
    return eventjson.json()


def get_event(args, token):
    """Returns detailed information about events

    Expects minimum one ID, or an array, then returns details about each ID

    Arguments:
        args {array} -- Array of arguments supplied from the commandline
        authtoken {string} -- The authentication token of the user

    Returns:
        array -- Returns an array of results, depending on how many id's was requested
    """
    # start time: 1728493154
    # end time: 1728496754
    url = "https://" + args.host + ":" + args.port + "/detect-api/rest/events/retrieve"
    x = [int(evid) for evid in args.eventid.split(",")]
    data = { 'ids':  x , 'startTime': 1, 'endTime': 1, }
    return esm_api_call(url, data, 'post', args.verifyssl, token)
    #2024/10/21 19:49:23 CEST



def main():
    urllib3.disable_warnings()
    args = parse_command_line()
    authtoken = login(args)
    print(datetime.datetime.now())
    print("This is the token: " + authtoken)
    events = get_event(args,authtoken)
    print(events)
    for i in events:
        print("Event ID: " + str(i['eventId']))
        print("Event Name: " + i['name'])


if __name__ == '__main__':
    main()