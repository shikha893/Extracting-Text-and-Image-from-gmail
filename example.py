from google_api import gmail

GMAIL_CREDENTIALS_PATH = 'credentials.json'
GMAIL_TOKEN_PATH = 'token.json'

search_query = "is:unread"
service = gmail.get_gmail_service(GMAIL_CREDENTIALS_PATH,
                                  GMAIL_TOKEN_PATH)
csvs_and_excel = gmail.query_for_csv_or_xl_attachments(service, search_query)

# 1st Attachment found:
if csvs_and_excel:
    print ("Success")
    