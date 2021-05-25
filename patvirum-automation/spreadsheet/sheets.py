from __future__ import print_function

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from settings import SCOPES, SPREADSHEET_ID, CREDENTIALS, TOKEN_PICKLE

import logging as LOG

class Sheets:

    def __init__(self, spreadsheet_id, credentials=CREDENTIALS, token_pickle=TOKEN_PICKLE):
        creds = None
        if os.path.exists(os.path.abspath(token_pickle)):
            with open(os.path.abspath(token_pickle), 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.path.abspath(credentials), SCOPES)
                creds = flow.run_local_server(port=0)

            with open(os.path.abspath(token_pickle), 'wb') as token:
                pickle.dump(creds, token)

        self.spreadsheet_id = spreadsheet_id
        self.service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

        # Call the Sheets API
        self.file = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[]).execute()

        # LOG.info(f"Request to the SpreadSheet: [{DOC_URL%self.spreadsheet_id}]")

    def get_sheets_name(self):
        return [sheet['properties']['title'] for sheet in self.file['sheets']]

    def get_sheet_values(self, sheet_name):
        return self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=sheet_name, valueRenderOption='FORMATTED_VALUE').execute()


if __name__ == '__main__':


    CREDENTIALS = 'credentials.json'
    TOKEN_PICKLE = 'token.pickle'

    sheet = Sheets(SPREADSHEET_ID, CREDENTIALS, TOKEN_PICKLE)
    print(sheet.get_sheet_values("Products").get('values', []))