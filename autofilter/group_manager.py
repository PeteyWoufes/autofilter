# pylint:disable=E1101
from __future__ import print_function
from googleapiclient.discovery import build
import google.oauth2
from oauth2client.service_account import ServiceAccountCredentials
import json
import googleapiclient
from httplib2 import Http
import requests


def main(google_api):
    ''' Sets poweruser value. "poweruser" is the administrator for the company's G Suite. '''
    poweruser = "testaccount@yourdomain.com"
    ''' Gets service account credentials '''
    credentials = google_api.getCreds()
    ''' Opens a .json file to find the list of groups to create and users to add. '''
    with open("groups.json", 'r') as a:
        data = json.loads(a.read())
    ''' Creates a group with each value in the "groups" section of groups.json '''
    for group in data["groups"]:
        addGroup(data, group, poweruser, credentials)
    ''' Adds each user to all the groups in groups.json. '''
    for user in data["users"]:
        for groups in data["groups"]:
            addUser(data, user, groups, poweruser, credentials)


def addUser(data, user, groups, poweruser, credentials):
    ''' Impersonates the administrator (poweruser) and builds a service to access the Directory API '''
    delegated_creds = credentials.create_delegated(poweruser)
    service = build(serviceName='admin', version='directory_v1',
                    http=delegated_creds.authorize(Http()))

    ''' Sets the user to add to the group (bodyInfo) and the group to add them to (groupInfo) '''
    bodyInfo = {"email": user}
    groupInfo = groups
    try:
        ''' Tries to add user to the group '''
        service.members().insert(body=bodyInfo, groupKey=groupInfo).execute()
        ''' Confirmation Message '''
        print(user + " is now a member of " + groups)
    except:
        ''' Error message when unable to add user to group '''
        print("Unable to make " + user + " a member of " + groups)


def addGroup(data, group, poweruser, credentials):
    ''' Impersonates the administrator (poweruser) and builds a service to access the Directory API '''
    delegated_creds = credentials.create_delegated(poweruser)
    service = build(serviceName="admin", version="directory_v1",
                    http=delegated_creds.authorize(Http()))
    ''' Sets the groupKey of the group '''
    groupInfo = {"email": group}
    try:
        ''' Tries to create group '''
        service.groups().insert(body=groupInfo).execute()
        ''' Confirmation Message '''
        print("The group " + group + " now exists.")
    except:
        ''' Error message when unable to create group '''
        print("Unable to create " + group)

