
from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
  creds = tools.run_flow(flow, store)
service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

form_id1 = "1fWXd3P86_7lBUViQ7zZU1cp_-fotA5iLQp8G56g0KUg"





def read_gform(form_id):
    result = service.forms().responses().list(formId=form_id).execute()
    
    respondent_email = []
    if 'responses' in result:
        for response in result['responses']:
            if 'respondentEmail' in response:
                respondent_email.append(response['respondentEmail'])
    return respondent_email

print(read_gform(form_id1))
                