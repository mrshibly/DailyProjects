import os
import pickle
import time
import glob
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate():
    """Authenticate the user and return the Google Drive API client."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = Credentials.from_authorized_user(token, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file(service, file_path, folder_id):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    try:
        file = service.files().create(
            body=file_metadata, media_body=media, fields='id').execute()
        print(f'File {file_name} uploaded with ID {file.get("id")}')
    except Exception as e:
        print(f'An error occurred: {e}')

def backup_files(folder_path, folder_id):
    """Backup files from the specified folder to Google Drive."""
    service = authenticate()
    files = glob.glob(os.path.join(folder_path, '*'))
    if not files:
        print(f"No files found in the folder: {folder_path}")
    for file_path in files:
        upload_file(service, file_path, folder_id)

if __name__ == '__main__':
    local_folder = input("Enter the path to the local folder you want to backup: ").strip()
    while not os.path.exists(local_folder):
        print("The provided path does not exist. Please try again.")
        local_folder = input("Enter the path to the local folder you want to backup: ").strip()
    
    drive_folder_id = input("Enter the ID of the Google Drive folder to upload to: ").strip()
    while not drive_folder_id:
        print("Google Drive folder ID cannot be empty. Please try again.")
        drive_folder_id = input("Enter the ID of the Google Drive folder to upload to: ").strip()

    print(f"Local folder: {local_folder}")
    print(f"Google Drive folder ID: {drive_folder_id}")
    confirm = input("Is the above information correct? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Aborting backup process.")
        exit()

    print("Starting the backup process...")
    while True:
        backup_files(local_folder, drive_folder_id)
        print("Backup completed. Next backup in 24 hours.")
        time.sleep(86400)  # Run backup every 24 hours
