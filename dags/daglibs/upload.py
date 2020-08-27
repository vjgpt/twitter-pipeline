from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import subprocess
import os
from os.path import join


path = os.getcwd()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # Backup the tweets
    subprocess.call(['tar -czvf tweet.tar.gz /usr/local/airflow/data/', '-1'], shell=True)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    print (join(path,'dags/daglibs/token.pickle'))
    if os.path.exists(join(path,'dags/daglibs/token.pickle')):
        with open(join(path,'dags/daglibs/token.pickle'), 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(join(path,
                'dags/daglibs/credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(join(path,'dags/daglibs/token.pickle'), 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    file_metadata = {'name': 'tweet.tar.gz'}
    media = MediaFileUpload('/usr/local/airflow/tweet.tar.gz', mimetype='*/*')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ("File ID: {}".format(file.get('id')))
    if file.get('id'):
        return True
    return False

if __name__ == '__main__':
    main()
