# pylint:disable=E1101
import googleapiclient
from googleapiclient.discovery import build
from httplib2 import Http
import autofilter.google_api as google_api


def batch_add(config):
    ''' This function creates a filter based on what's in the config file and adds it to all specified users' accounts. '''
    for user in config["users"]:
        ''' Builds a service to access the Gmail API. '''
        service = google_api.buildService(google_api, user)
        for google_filter in config['filters']:
            ''' Converts data in config file to format usable by Gmail. '''
            filter_data = config['filters'][google_filter]
            body = {"criteria": filter_data['criteria'],
                    "action": filter_data['action']}

            ''' Creates filter using Gmail API. '''
            __add(service, body)
            ''' Confirmation Message. '''
            print("Filter " + str(google_filter) + " successfully created.")


''' Public Access Point for creation of filters. '''


def add(user, filter_object):
    ''' Builds service to access Gmail API. '''
    service = google_api.buildService(user, "gmail")
    __add(service, filter_object)





def __add(service, filter_object):
    ''' Add a single filter to a user's account. '''
    service.users().settings().filters().\
        create(userId="me", body=filter_object).execute()

def create_filter_object(crit, labels, labelName):
    for label in labels:
        if label["name"] == labelName:
            ''' Matches labelID to labelName. At present Google does not provide this functionality through their API: very important not to delete. '''
            labelID = label["id"]
            break
    action = {"addLabelIds": [labelID]}
    ''' Builds request body for creating the filter. '''
    body = {"criteria": crit,
                    "action": action}
    return body
