from googleapiclient.discovery import build
from httplib2 import Http


def batch_add(google_api, data):
    ''' Data must be passed in in the format laid out in the config template. '''
    for user in data["users"]:
        ''' Builds the service needed to access the Gmail API. '''
        service = google_api.buildService(user)
        for label in data["labels"]:
            label_str = str(label)
            label_object = {'messageListVisibility': "show",
                            'name': label_str, 'labelListVisibility': "labelShow"}
            ''' Calls function to add the label to the users' account. '''
            __add(service, user, label_object)

''' public entry for single label create'''
def add(google_api, user, label_object):
    service = google_api.buildService(user)
    __add(service, user, label_object)


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


