from googleapiclient.discovery import build
from httplib2 import Http
import json

def fetch_labels(google_api, user):
    ''' Builds service to access Gmail API. '''
    service = google_api.buildService(user, "gmail")
    ''' Queries Gmail API to check what labels are present on user's Gmail account. '''
    response = service.users().labels().list(userId=user).execute()
    labels = response['labels']
    for label in labels:
        ''' Prints labels with their names and IDs. '''
        print ('Label id: %s - Label name: %s' % (label['id'], label['name']))
    return (labels)