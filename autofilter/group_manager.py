# pylint:disable=E1101
from __future__ import print_function

import json

import google.oauth2
import googleapiclient
import requests
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
import autofilter.google_api as google_api


def loadGroups():
    with open("groups.json", 'r') as a:
        data = json.loads(a.read())
    return data


def bulkAddUser():
    data = loadGroups()
    ''' Sets the user to add to the group (bodyInfo) and the group to add them to (groupInfo) '''
    for group in data["groups"]:
        for user in data["users"]:
            service = google_api.buildService(None, "directory")
            bodyInfo = {"email": user}
            ''' Tries to add user to the group. '''
            service.members().insert(body=bodyInfo, groupKey=group).execute()
            ''' Confirmation Message '''
            print(user + " is now a member of " + group)

def addUser(user, group):
    service = google_api.buildService(None, "directory")
    bodyInfo = {"email": user}
    ''' Tries to add user to the group. '''
    try:
        service.members().insert(body=bodyInfo, groupKey=group)
        print(user + " is now a member of " + group)
    except:
        print("Unable to add " + user + " to " + group)
def createGroup(group):
    ''' Impersonates the administrator (poweruser) and builds a service to access the Directory API '''
    service = google_api.buildService(None, "directory")
    ''' Sets the groupKey of the group '''
    groupInfo = {"email": group}
    ''' Tries to create group '''
    service.groups().insert(body=groupInfo).execute()
    ''' Confirmation Message '''
    print("The group " + group + " now exists.")


def listUsers(show):
    ''' Loads group data. '''
    data = loadGroups()
    for user in data["users"]:
        ''' Builds service to access the Directory API. '''
        service = google_api.buildService(None, "directory")
        ''' Queries the Directory API and gets a list of the groups the user is in. '''
        results = service.groups().list(
            userKey=user, domain=data["domain"][0]).execute()
        response = json.dumps(results, indent=4, separators=(",", ";"))
        ''' Prints response. '''
        print(response)
