# 🔒 EncryptoLock

Welcome to **EncryptoLock** - your secure password manager that stores and retrieves passwords securely using encryption! 

## 🌟 Features

- 🔐 **Secure Storage**: Encrypts your passwords using `cryptography`.
- 🗃️ **Data Persistence**: Saves passwords to a JSON file.
- 🔍 **Easy Retrieval**: Quickly retrieve your encrypted passwords.
- 🧹 **Delete Functionality**: Easily delete passwords when no longer needed.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `cryptography` library

### Installation

1. Clone the repository

2. Install the required libraries:

    ```sh
    pip install cryptography
    ```

3. Run the script:

    ```sh
    python EncryptoLock.py
    ```

## 🛠️ Usage

Once you run the script, you'll be greeted with a command-line interface:

```plaintext
Welcome to EncryptoLock

Options:
1. Add password
2. Get password
3. Delete password
4. Exit
Enter choice:
```

### Add a Password

1. Select option `1`.
2. Enter the service name.
3. Enter the username.
4. Enter the password.

### Retrieve a Password

1. Select option `2`.
2. Enter the service name.
3. The password will be displayed if it exists.

### Delete a Password

1. Select option `3`.
2. Enter the service name.
3. The password will be deleted if it exists.

### Exit

1. Select option `4` to exit the program.

## 📂 Project Structure

```plaintext
EncryptoLock/
│
├── EncryptoLock.py     # Main script
├── secret.key          # Encryption key (generated automatically)
└── passwords.json      # JSON file to store encrypted passwords
```

## 🧑‍💻 Contributing

Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or feedback, please contact [mahmudurrahman858@gmail.com](mailto:mahmudurrahman858@gmail.com).
