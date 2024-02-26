from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from regex_for_links import extract_sheet_id 

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyAtd9ruNYabKdh7R65BuIW1xOXnZYC2qPM'

#the link of the google sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/13m82LlEeHzvgZ3iLTByvFp21mjG5-gXC6rezX0qcjYM/edit#gid=0'
sheet_id = extract_sheet_id(sheet_url)


def get_cell_value(spreadsheet_id, range, i):
    # Load credentials from JSON file
    credentials = Credentials.from_service_account_file('credentials.json')

    # Build service with credentials
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API to get values
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range).execute()

    # Get values from response
    values = result.get('values', [])

    # Extract value from cell B2
    if not values:
        print('No data found.')
        return None
    else:
        # Assuming B2 is not empty
        email = values[i][1]  # B2 is the first and only cell
        return email

# Example usage
range = 'Sheet1!A1:D'  # Range for cell B2

email_array = []
i = 1
while i < 3:
  
  email_array.append(get_cell_value(sheet_id, range,i))
  i += 1

print(email_array)
