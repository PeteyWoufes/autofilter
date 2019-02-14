# pylint:disable=E1101
from __future__ import print_function

import json

import google.oauth2
import googleapiclient
import requests
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


def loadGroups():
    with open("groups.json", 'r') as a:
        data = json.loads(a.read())
    return data


def addUser(google_api, show):
    data = loadGroups()
    delegated_creds = getAuth(google_api)
    service = build(serviceName='admin', version='directory_v1',
                    http=delegated_creds.authorize(Http()))

    ''' Sets the user to add to the group (bodyInfo) and the group to add them to (groupInfo) '''
    for group in data[show]["groups"]:
        for user in data[show]["users"]:
            bodyInfo = {"email": user}
            ''' Tries to add user to the group '''
            service.members().insert(body=bodyInfo, groupKey=group).execute()
            ''' Confirmation Message '''
            print(user + " is now a member of " + group)


def addGroup(group, google_api):
    ''' Impersonates the administrator (poweruser) and builds a service to access the Directory API '''
    delegated_creds = getAuth(google_api)
    service = build(serviceName="admin", version="directory_v1",
                    http=delegated_creds.authorize(Http()))
    ''' Sets the groupKey of the group '''
    groupInfo = {"email": group}

    ''' Tries to create group '''
    service.groups().insert(body=groupInfo).execute()
    ''' Confirmation Message '''
    print("The group " + group + " now exists.")


def getAuth(google_api):
    credentials = google_api.getCreds()
    with open("auth.json", 'r') as a:
        data = json.loads(a.read())
    poweruser = data["poweruser"][0]
    delegated_creds = credentials.create_delegated(poweruser)
    return delegated_creds


def listUsers(google_api, show):
    data = loadGroups()
    delegated_creds = getAuth(google_api)
    for user in data[show]["users"]:
        service = build("admin", "directory_v1",
                        http=delegated_creds.authorize(Http()))
        results = service.groups().list(
            userKey=user, domain=data[show]["domain"][0]).execute()
        response = json.dumps(results, indent=4, separators=(",", ";"))
        print(response)
