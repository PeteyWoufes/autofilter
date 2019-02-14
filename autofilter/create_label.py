from googleapiclient.discovery import build
from httplib2 import Http
import autofilter.google_api as google_api


def batch_add(google_api, data):
    ''' Data must be passed in in the format laid out in the config template. '''
    for user in data["users"]:
        ''' Builds the service needed to access the Gmail API. '''
        service = google_api.buildService(user, "gmail")
        for label in data["labels"]:
            label_str = str(label)
            label_object = __create_label_object(label_str)
            ''' Calls function to add the label to the users' account. '''
            __add(service, user, label_object)

''' Public Access Point for creation of single label. '''
def add(user, label_str):
    ''' Builds label object to add to user's Gmail account. '''
    label_object = __create_label_object(label_str)
    service = google_api.buildService(user, "gmail")
    label = __add(service, user, label_object)
    return label


def __add(service, user, label_object):
    ''' Tries to add label to user account. Prints confirmation if successful, error if not. '''
    try:
        ''' Accesses the Gmail API using the service created earlier. '''
        label = service.users().labels().create(
            userId=user, body=label_object).execute()
        label_str = str(label)
        print('Label ' + label_str + ' successfully created.')
        return label
    except:
        print('Unable to create label.')

def __create_label_object(label_str):
    ''' Creates a label object in a format usable by Gmail. '''
    label_object = {'messageListVisibility': "show",
                            'name': label_str, 'labelListVisibility': "labelShow"}
    return label_object