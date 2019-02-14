from googleapiclient.discovery import build
from httplib2 import Http
import json

def fetch_labels(google_api, user):
    service = google_api.buildService(user, "gmail")
    response = service.users().labels().list(userId=user).execute()
    labels = response['labels']
    for label in labels:
        print ('Label id: %s - Label name: %s' % (label['id'], label['name']))
    return (labels)