from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

creds= 'credentials.json'
DRIVE_FOLDER_ID = '1wj-Qw4iTDqkUsIJ-_AjnkGrOPHhTG1da'





def create_gform(name, titles):
    creds = service_account.Credentials.from_service_account_file('credentials.json')

    form_service = googleapiclient.discovery.build('forms', 'v1', credentials=creds)
    NEW_FORM = {
    "info": {
        "title": name,
       
    }
    }
    requests_list = []
    for index, title in enumerate(titles, start=0):
        request = {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": False,
                        "textQuestion": {"paragraph" : True},
                        
                    }
                }
            },
            "location": {"index": index}
        }
    }
        requests_list.append(request)

    NEW_QUESTION = {"requests": requests_list}
# Creates the initial form
    result = form_service.forms().create(body=NEW_FORM).execute()

# Adds the question to the form
    question_setting = (form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute())

# Prints the result to show the question has been added
    get_result = form_service.forms().get(formId=result["formId"]).execute()
    #print(get_result)
    return(get_result['responderUri'])

