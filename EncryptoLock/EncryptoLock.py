import os
import json
from cryptography.fernet import Fernet
import getpass

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message
  
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

class EncryptoLock:
    def __init__(self, storage_file="passwords.json"):
        self.storage_file = storage_file
        self.key = self._get_key()
        self.data = self._load_data()

    def _get_key(self):
        if not os.path.exists("secret.key"):
            generate_key()
        return load_key()

    def _load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                return json.load(f)
        return {}

    def _save_data(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.data, f)

    def add_password(self, service, username, password):
        encrypted_password = encrypt_message(password, self.key)
        self.data[service] = {"username": username, "password": encrypted_password.decode()}
        self._save_data()

    def get_password(self, service):
        if service in self.data:
            encrypted_password = self.data[service]["password"]
            return decrypt_message(encrypted_password.encode(), self.key)
        else:
            return None

    def delete_password(self, service):
        if service in self.data:
            del self.data[service]
            self._save_data()

def main():
    manager = EncryptoLock()
    print("Welcome to EncryptoLock")
    while True:
        print("\nOptions:")
        print("1. Add password")
        print("2. Get password")
        print("3. Delete password")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            manager.add_password(service, username, password)
            print("Password added successfully.")

        elif choice == '2':
            service = input("Enter service name: ")
            password = manager.get_password(service)
            if password:
                print(f"Password for {service} is {password}")
            else:
                print("Service not found.")

        elif choice == '3':
            service = input("Enter service name: ")
            manager.delete_password(service)
            print("Password deleted successfully.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
