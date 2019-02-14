import json

from googleapiclient.discovery import build
from google.oauth2 import service_account
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


def getCreds():
    ''' This function gets the Service Account Credentials for your domain so autofilter can impersonate each of your users. '''
    ''' Reads all auth information from a JSON file you will need to configure. '''
    with open("auth.json", 'r') as a:
        data = json.loads(a.read())
    ''' Google provides each Service Account with a unique email. '''
    serviceaccountemail = data["service_account_email"][0]
    ''' This is the path to a keyfile you should be given by your G Suite Administrator. '''
    serviceaccountpkcs12filepath = data["service_account_pkcs12_file_path"][0]
    password = data["password"][0]
    ''' Scopes need to be authorized by a G Suite administrator in the "advanced settings" section. '''
    scopes = data["scopes"]
    ''' This generates your credentials using all the information acquired above. '''
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        serviceaccountemail, serviceaccountpkcs12filepath, password, scopes=scopes)
    return credentials

def buildService(user, API):
    if API == "gmail":
        ''' Gets service account credentials. '''
        credentials = getCreds()
        ''' Impersonates user to modify their Gmail. '''
        delegated_creds = credentials.create_delegated(user)
        ''' Builds service to access Gmail API. '''
        service = build(
            'gmail', 'v1', http=delegated_creds.authorize(Http()))
        return service

    if API == "directory":
        ''' Gets service account credentials. '''
        credentials = getCreds()
        ''' Reads from auth file to find the identity of a G Suite administrator. '''
        with open("auth.json", 'r') as a:
            data = json.loads(a.read())
        ''' Poweruser is a G Suite adminstrator. '''
        poweruser = data["poweruser"][0]
        ''' Uses service account credentials to impersonate poweruser. '''
        delegated_creds = credentials.create_delegated(poweruser)
        ''' Builds service to access the Directory API. '''
        service = build(serviceName="admin", version="directory_v1",
                    http=delegated_creds.authorize(Http()))
        return service
