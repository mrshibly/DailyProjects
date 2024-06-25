# 🚀 AutoDriveSync

AutoDriveSync is an automated data backup system that uploads files from a specified local folder to a Google Drive folder at regular intervals using Python.

## ✨ Features

- 🔐 Authenticates with Google Drive using OAuth 2.0
- 📂 Backs up files from a local folder to a specified Google Drive folder
- ⏰ Runs backups every 24 hours
- ⚠️ Handles errors gracefully and provides user-friendly messages

## 🛠 Prerequisites

- 🐍 Python 3.6 or higher
- ☁️ Google Cloud project with Google Drive API enabled
- 📄 Credentials file (`credentials.json`) from Google Cloud Console

## 📥 Installation

1. **Install the required Python packages:**

    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

2. **Download the credentials file:**
   
   Go to the [Google Cloud Console](https://console.cloud.google.com/), create a new project, enable the Google Drive API, and download the `credentials.json` file. Place this file in the root directory of your project.

## 🚀 Usage

1. **Run the backup script:**

    ```bash
    python backup_to_gdrive.py
    ```

2. **Follow the prompts:**

   - Enter the path to the local folder you want to back up.
   - Enter the ID of the Google Drive folder where the files will be uploaded.

3. **Confirm the information:**

   - The script will display the provided paths and ask for confirmation.
   - Type `yes` to start the backup process or `no` to abort.

4. **Backup process:**

   - The script will authenticate with Google Drive and start the backup process.
   - It will run the backup every 24 hours automatically.

## 📝 Example

Here is an example of running the script:

```bash
$ python backup_to_gdrive.py
Enter the path to the local folder you want to backup: /path/to/local/folder
Enter the ID of the Google Drive folder to upload to: your_drive_folder_id
Local folder: /path/to/local/folder
Google Drive folder ID: your_drive_folder_id
Is the above information correct? (yes/no): yes
Starting the backup process...
File example.txt uploaded with ID 1a2b3c4d5e6f
Backup completed. Next backup in 24 hours.
```

## ⚠️ Error Handling

- If the local folder path does not exist, the script will prompt you to enter a valid path.
- If the Google Drive folder ID is empty, the script will prompt you to enter a valid ID.
- Any errors during the file upload process will be caught and displayed.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit suggestions or report issues.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- This project uses the [Google Drive API](https://developers.google.com/drive/api) to interact with Google Drive.
- Inspired by various open-source backup solutions.
