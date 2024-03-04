from flask import Flask, render_template, request
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
import googleapiclient.discovery
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from regex_for_links import extract_sheet_id
from create_gsp import create_spreadsheet
from get_cell_values import get_cell_values
 


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
SERVICE_ACCOUNT_FILE = 'credentials.json'
# Authorize the clientsheet 
client = gspread.authorize(creds)


# The ID of the Google Drive folder where you want to create the spreadsheet
DRIVE_FOLDER_ID = '1wj-Qw4iTDqkUsIJ-_AjnkGrOPHhTG1da'



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form1_data = request.form['form1']
    form2_data = request.form['form2']
    form3_data = request.form['form3']
    
    # Here you can use the form data as needed
    print("Form 1 data:", form1_data)
    print("Form 2 data:", form2_data)
    print("Form 3 data:", form3_data)
    sheet_id = extract_sheet_id(form2_data)
    
    # For example, you can return a response with the form data
    sheet_id = extract_sheet_id(form2_data)
    
    
    num = str(int(form1_data) + 1)
    range = "Sheet1!A2:D"+num  # Range for cell A2 to D{whatever number the user puts}
        
    cell_values = [[]]
    cell_values = (get_cell_values(sheet_id, range))
    new_sheet_link = create_spreadsheet(form3_data)
    spreadsheet = client.open_by_key(extract_sheet_id(new_sheet_link))
    worksheet = spreadsheet.worksheet('Sheet1')
    m_list = []
    i = 0
    # Loop to generate the lists
    while i<int(form1_data):

        # Create a list containing a single random number
        row = [random.randint(1, 40)]
        # Append the list to the main list
        m_list.append(row)
        i = i+1


    num2 = "A2:C"+str(int(form1_data)+1)
    num3 = "D2:D1"+str(int(form1_data)+1)
    casual_values = [["Name", "ID", "Email", "Number"]]
    worksheet.update("A1:D1",casual_values )
    worksheet.update(num2,cell_values)

    worksheet.update(num3, m_list)
    return render_template('other.html', user_id=new_sheet_link)   


if __name__ == '__main__':
    app.run(debug=True)

