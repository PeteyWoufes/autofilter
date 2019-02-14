import json

from apiclient import errors
from google.oauth2 import service_account
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, service_account, tools
from oauth2client.service_account import ServiceAccountCredentials


def getCreds():
    ''' Reads from a .json file '''
    with open("auth.json", 'r') as a:
        data = json.loads(a.read())
    serviceaccountemail = data["service_account_email"][0]
    ''' This is the path to a keyfile you should be given by your G Suite Administrator. '''
    serviceaccountpkcs12filepath = data["service_account_pkcs12_file_path"][0]
    password = data["password"][0]
    ''' Scopes need to be authorized by a G Suite administrator in the "advanced settings" section. '''
    scopes = data["scopes"]
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        serviceaccountemail, serviceaccountpkcs12filepath, password, scopes=scopes)
    return credentials


def printHi():
    print("hi")
