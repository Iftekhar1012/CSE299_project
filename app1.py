from flask import Flask, render_template, request, redirect, url_for, session, abort
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
from create_gform import create_gform
#from receive_gform import read_gform
from pdf_reader import extract_text_from_pdf
from sending_emails2 import send_email
import os
import pathlib
import requests
from flask import Flask, session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Autograder")
app.secret_key = "llm_autograder"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "754691320592-i0ctlblbr8mct068bnkdi0bf36a22ibj.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)



def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
SERVICE_ACCOUNT_FILE = 'credentials.json'
# Authorize the clientsheet 
client = gspread.authorize(creds)


# The ID of the Google Drive folder where you want to create the spreadsheet
DRIVE_FOLDER_ID = '1wj-Qw4iTDqkUsIJ-_AjnkGrOPHhTG1da'

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return render_template('login.html')
   


@app.route("/protected_area")
@login_is_required
def protected_area():
    return render_template('main.html', user_email = session["name"] )








@app.route('/submit', methods=['POST'])
def Submit():
    # Retrieve form data
    form1_data = request.form['textbox1']
    form2_data = request.form['textbox2']
    form3_data = request.form['textbox3']
    files = []
    UPLOAD_FOLDER = 'uploads'
    if 'files[]' not in request.files:
        return 'No file part'
    files = request.files.getlist('files[]')
    for file in files:
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Files uploaded successfully'



    
    # Extract text from the PDF file
    #pdf_text = extract_text_from_pdf(pdf_file_path)
    
    # Print the extracted text
    print(pdf_text)
    
    # Here you can use the form data as needed
    print("Form 1 data:", form1_data)
    print("Form 2 data:", form2_data)
    print("Form 3 data:", form3_data)
    sheet_id = extract_sheet_id(form1_data)
    
    # For example, you can return a response with the form data
    sheet_id1 = extract_sheet_id(form2_data)
    
    
    
    range = "Sheet1!A2:C100" 
        
    cell_values = [[]]
    cell_values = (get_cell_values(sheet_id, range))
    num = len(cell_values)
    cell_values1 = [[]]
    cell_values1 = (get_cell_values(sheet_id1, range))
    num1 = len(cell_values1)

    """""
    new_sheet_link = create_spreadsheet(form3_data)
    spreadsheet = client.open_by_key(extract_sheet_id(new_sheet_link))
    worksheet = spreadsheet.worksheet('Sheet1')
    m_list = []
    """
    
    # Loop to generate the lists
    email = []
    questions = []
    i = 0
    j = 0
    while i<num:
        email.append(cell_values[i][2])
        i = i+1

    while j<num1:
        questions.append(cell_values1[j][0])
        j = j+1
    

    
    
    gformlink = create_gform(form3_data, questions)
    text = "Here's the link to the Google form "+ gformlink 
    send_email(email, text)

     


    

    """""
    num2 = "A2:C"+str(int(num)+1)
    num3 = "D2:D1"+str(int(num)+1)
    casual_values = [["Name", "ID", "Email", "Number"]]
    worksheet.update("A1:D1",casual_values )
    worksheet.update(num2,cell_values)

    worksheet.update(num3, m_list)

    """
    return render_template('other.html', user_id=gformlink, pdf_text = pdf_text)   





if __name__ == "__main__":
    app.run(port = 5000,debug=True)