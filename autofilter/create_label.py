from __future__ import print_function

import json

from googleapiclient.discovery import build
from httplib2 import Http

import autofilter.clear_files as CF

"""
def MakeLabel(label_name, mlv='show', llv='labelShow'):
    ''' Creates label object using default visibility settings and a label name provided in the parameters. '''
    label = {'messageListVisibility': mlv,
             'name': label_name, 'labelListVisibility': llv}
    return label
"""

def CreateLabel(service, user_id, label_object):
    ''' Attempts to create a label using the label object creating earlier. '''
    try:
        label = service.users().labels().create(
            userId=user_id, body=label_object).execute()
        label_str = str(label)
        ''' Confirmation Message '''
        print('Label ' + label_str + ' successfully created.')
        return label
    except:
        ''' Error message when unable to create label. '''
        print('Unable to create label.')
''' WE want to be able to take in a number of dynamic use cases for this, external data including users,labels,filters '''
def addLabels(google_api, data):
    CF.delete_ids()
    ''' Override external data source (Test)'''
    data = getData()
    for user in data["users"]:
        service = getAuth(google_api, user)
        for label in data["labels"]:
            label_str = str(label)
            label_object = {'messageListVisibility': "show",
             'name': label_str, 'labelListVisibility': "labelShow"}
            #label_object = MakeLabel(label_str, mlv="show", llv="labelShow")
            label_data = CreateLabel(service, user, label_object)
            with open("id.txt", "a") as f:
                f.write(label_data["name"] + ":" + label_data["id"])


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

def write_to_ids_user(user, labelDict):
    labelDict["users"] = user
    labelDict["users"][user] = "ids"
