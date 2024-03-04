import os
from google.oauth2 import service_account
import googleapiclient.discovery

SERVICE_ACCOUNT_FILE = 'credentials.json'


DRIVE_FOLDER_ID = '1wj-Qw4iTDqkUsIJ-_AjnkGrOPHhTG1da'




def create_spreadsheet(title2):
    # Authenticate with Google Sheets API using service account credentials
    cred = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=cred)

    # Creates a new spreadsheet
    spreadsheet = service.spreadsheets().create(body={
        'properties': {
            'title': title2
        }
    }).execute()

    # Get the ID of the newly created spreadsheet
    spreadsheet_id = spreadsheet['spreadsheetId']

    # Share the spreadsheet with anyone with the link
    drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=cred)
    drive_service.permissions().create(
        fileId=spreadsheet_id,
        body={'type': 'anyone', 'role': 'writer'}
    ).execute()
    
    sps_id = spreadsheet_id
    print(sps_id)
    
    return("https://docs.google.com/spreadsheets/d/"+sps_id+"/edit#gid=0")

title = "My second auto"
if __name__ == "__main__":
    print(create_spreadsheet(title))
    
