from __future__ import print_function

import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from settings import CREDENTIALS_FILE

TOKEN_FILE = os.path.join(os.getcwd(), 'token.pickle')

# everything having to do with the google api account


class HorribleGoogleAPIService(object):

    SCOPES = ['https://www.googleapis.com/auth/presentations']

    def __init__(self):
        self.creds = self._creds()

    @property
    def slides_service(self):
        return build('slides', 'v1', credentials=self.creds)

    def _creds(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)

        return creds
