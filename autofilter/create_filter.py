# pylint:disable=E1101
from __future__ import print_function
from googleapiclient.discovery import build

import json
import googleapiclient
from httplib2 import Http
import requests


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
            results = service.users().labels().list(userId='me').execute()
            ''' Creates a filter for each of the filters in the list. '''
            for google_filter in data[department]['filters']:
                create_filter(results, service,
                              google_filter)


def create_filter(labels, service, google_filter):
    ''' Tries to create filter using parameters set earlier. '''
    try:
        service.users().settings().filters().\
        create(userId="me", body=google_filter).execute()
        ''' Confirmation Message '''
        print ("Filter " + google_filter + " successfully created.")
    except:
        ''' Error message when unable to create filter. '''
        print("Unable to create filter: " + google_filter)

