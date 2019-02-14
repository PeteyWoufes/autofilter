# pylint:disable=E1101
from __future__ import print_function
from googleapiclient.discovery import build

import json
import googleapiclient
from httplib2 import Http
import requests


"""
def main(google_api):
    ''' Gets service account credentials '''
    credentials = google_api.getCreds()
    ''' Opens a .json file to find the list of filters to create and accounts to add these filters to. '''
    with open("config.json", 'r') as a:
        data = json.loads(a.read())
    for department in data:
        for user in data[department]["users"]:
            ''' Impersonates each user with the service account credentials acquired earlier. '''
            delegated_creds = credentials.create_delegated(user)
            ''' Builds a service to access the Gmail API. '''
            service = build(
                'gmail', 'v1', http=delegated_creds.authorize(Http()))
            ''' Creates a filter for each of the filters in the list. '''
            for google_filter in data[department]['filters']:
                filter_data = json.loads(json.dumps(data[department]['filters'][google_filter]))
                body = {"criteria": filter_data['criteria'], "action": filter_data['action']}
                # create_filter(service, body)
"""

def create_filter(google_api, data):
    
    config = getConfig()
    for user in config["users"]:
        service = getAuth(google_api, user)
        for google_filter in config['filters']:
                filter_data = config['filters'][google_filter]
                body = {"criteria": filter_data['criteria'], "action": filter_data['action']}
                
                ''' Tries to create filter using parameters set earlier. '''
                service.users().settings().filters().\
                    create(userId="me", body=body).execute()
                ''' Confirmation Message '''
                print("Filter " + str(google_filter) + " successfully created.")
            

def getConfig():
    with open("config.json", 'r') as a:
        config = json.loads(a.read())
    return config

def getIDs():
    with open("id.txt", "r") as file:
        ids_file = json.loads(file.read())
    return ids_file

def getAuth(google_api, user):
    credentials = google_api.getCreds()
    delegated_creds = credentials.create_delegated(user)
    service = build('gmail', 'v1', http=delegated_creds.authorize(Http()))
    return service