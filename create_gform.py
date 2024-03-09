from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
  creds = tools.run_flow(flow, store)

form_service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

def create_gform(title, questions):
   NEW_FORM = {
    "info": {
        "title": title,
       
       
    }
    }
   requests_list = []  # Initialize an empty list to store the requests
   for index, title in enumerate(questions, start=0):
    request = {
        "createItem": {
            "item": {
                "title": questions,
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

