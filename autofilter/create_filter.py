# pylint:disable=E1101
import googleapiclient
from googleapiclient.discovery import build
from httplib2 import Http


def batch_add(google_api, config):
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
def add(google_api, user, filter_body):
    service = google_api.buildService(google_api, user)
    __add(service, filter_body)

''' Add a single filter to a user's account. '''
def __add(service, filter_body):
    service.users().settings().filters().\
                create(userId="me", body=filter_body).execute()
