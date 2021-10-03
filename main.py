from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint

SERVICE_ACCOUNT_FILE = 'keys.json'          #path for your json key.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)


# The ID of spreadsheet.
SAMPLE_SPREADSHEET_ID = '1OUoGqc7ma7N1rfRZE*******fE6SNe2LrJT****YURs'   #spreadsheet ID
service = build('sheets', 'v4', credentials=creds)


sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Form Responses 1!A1:C2").execute()
values = result.get('values', [])
pprint(values)