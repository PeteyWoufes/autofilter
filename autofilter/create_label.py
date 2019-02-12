from __future__ import print_function
from googleapiclient.discovery import build

import json
# import google_api
from httplib2 import Http


def main(google_api):
    ''' Gets service account credentials '''
    credentials = google_api.getCreds()
    ''' Opens a .json file to find the list of labels to create and accounts to add these labels to. '''
    with open("config.json", 'r') as a:
        data = json.loads(a.read())

    for department in data:
        for user in data[department]['users']:
            ''' Impersonates each user with the service account credentials acquired earlier. '''
            delegated_creds = credentials.create_delegated(user)
            ''' Builds a service to access the Gmail API. '''
            service = build(
                'gmail', 'v1', http=delegated_creds.authorize(Http()))
            for label in data[department]['labels']:
                label_str = str(label)
                label_object = MakeLabel(
                    label_str, mlv='show', llv='labelShow')
                CreateLabel(service, user, label_object)
                return label


def MakeLabel(label_name, mlv='show', llv='labelShow'):
    ''' Creates label object using default visibility settings and a label name provided in the parameters. '''
    label = {'messageListVisibility': mlv,
             'name': label_name, 'labelListVisibility': llv}
    return label


def CreateLabel(service, user_id, label_object):
    ''' Attempts to create a label using the label object creating earlier. '''
    try:
        label = service.users().labels().create(
            userId=user_id, body=label_object).execute()
        label_str = str(label)
        ''' Confirmation Message '''
        print('Label ' + label_str + ' successfully created.')
    except:
        ''' Error message when unable to create label. '''
        print('Unable to create label.')

def addLabels(google_api, show):
    data = getData()
    for user in data[show]["users"]:
        service = getAuth(google_api, user)
        for label in data[show]["labels"]:
            label_str = str(label)
            label_object = MakeLabel(label_str, mlv="show", llv="labelShow")
            CreateLabel(service, user, label_object)
            return label

def getAuth(google_api, user):
    credentials = google_api.getCreds()
    delegated_creds = credentials.create_delegated(user)
    service = build(
                'gmail', 'v1', http=delegated_creds.authorize(Http()))
    return service

def getData():
    with open("config.json", 'r') as a:
        data = json.loads(a.read())
    return data