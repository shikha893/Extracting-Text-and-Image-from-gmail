import base64
import pandas as pd
from io import StringIO
import os
import base64
from apiclient import errors

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools



def get_gmail_service(credentials_path, token_path):
    store = file.Storage(token_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_path, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service.users()

#ZZZZ
def query_for_message_ids(service, search_query):
    """searching for an e-mail (Supports the same query format as the Gmail search box.
    For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com>
    is:unread")
    """
    result = service.messages().list(userId='me', q=search_query).execute()
    results = result.get('messages')
    if results:
        msg_ids = [r['id'] for r in results]
    else:
        msg_ids = []
    print(msg_ids)
    return msg_ids


def query_for_csv_or_xl_attachments(service, search_query):
    message_ids = query_for_message_ids(service, search_query)
	#GetAttachments(service, 'me', msg_id, prefix="")
    for msg_id in message_ids:
        print(msg_id)
        GetAttachments(service, 'me', msg_id, "C:/dnld/")
    return True
	
	
#------------------------------------
def GetAttachments(service, user_id, msg_id, prefix):
    """Get and store attachment from Message with given id.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    prefix: prefix which is added to the attachment filename on saving
    """
    message = service.messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
        if part['filename']:
            if 'data' in part['body']:
                data=part['body']['data']
            else:
                att_id=part['body']['attachmentId']
                att=service.messages().attachments().get(userId=user_id, messageId=msg_id,id=att_id).execute()
                data=att['data']
            file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
            path = prefix+part['filename']
            filename_t=part['filename']
            with open(path, 'wb') as f:
                f.write(file_data)