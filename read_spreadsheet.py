

import requests
from regex_for_links import extract_sheet_id 

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyAtd9ruNYabKdh7R65BuIW1xOXnZYC2qPM'

#the link of the google sheet
sheet_url = 'https://docs.google.com/spreadsheets/d/13m82LlEeHzvgZ3iLTByvFp21mjG5-gXC6rezX0qcjYM/edit#gid=0'

sheet_id = extract_sheet_id(sheet_url)


# Define the URL for accessing the Google Sheets API
url = f'https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1?key={api_key}'

# Make a GET request to retrieve data
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data:", response.text)