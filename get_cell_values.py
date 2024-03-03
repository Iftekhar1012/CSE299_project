from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from regex_for_links import extract_sheet_id

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)


SERVICE_ACCOUNT_FILE = 'credentials.json'
DRIVE_FOLDER_ID = '1wj-Qw4iTDqkUsIJ-_AjnkGrOPHhTG1da'


spreadsheet_id1 = 'https://docs.google.com/spreadsheets/d/18v1TACmkTx5S8S5lHi0m4o-WUXPYvVsw_RHkeYrAf6E/edit#gid=0' #For testing
spreadsheet_id2 = extract_sheet_id(spreadsheet_id1)

def get_cell_values(spreadsheet_id, range):
 
    credentials = Credentials.from_service_account_file('credentials.json')
    sheet_list =[[]]
 
    service = build('sheets', 'v4', credentials=credentials)

    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()


    values = result.get('values', [])

    
    if  values:
        sheet_list = values
        return sheet_list
    

range1 = "A2:C4"
print(get_cell_values(spreadsheet_id2, range1)) 