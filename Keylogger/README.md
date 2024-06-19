
# Python Keylogger

## Overview
This project is a simple keylogger written in Python. The keylogger captures key presses, including spaces and the Enter key, and logs them to a file named `key_log.txt`.

## Features
- Captures and logs all key presses.
- Logs spaces and Enter key.
- Exits when the Esc key is pressed.

## Installation

### Prerequisites
- Python 3.x
- `pynput` library

### Install `pynput`
You can install the required `pynput` library using pip:
```sh
pip install pynput
```

### Clone the Repository
Clone this repository to your local machine:
```sh
git clone https://github.com/yourusername/simple-keylogger.git
cd simple-keylogger
```

## Usage

### Running the Keylogger
To run the keylogger, execute the script:
```sh
python simple_keylogger.py
```

### Creating an Executable
You can create a standalone executable using `pyinstaller`. First, install `pyinstaller`:
```sh
pip install pyinstaller
```

Then, generate the executable:
```sh
pyinstaller --onefile --noconsole simple_keylogger.py
```

The executable will be created in the `dist` directory.

## Important Notes
- **Ethical Use**: This keylogger should only be used for educational purposes or within environments where you have explicit permission to monitor keystrokes.
- **Legal Disclaimer**: Unauthorized use of keyloggers is illegal and unethical. Ensure you have the necessary permissions before running this software on any machine.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## Acknowledgments
This project uses the [pynput](https://pypi.org/project/pynput/) library for capturing keyboard events.

### Steps to Follow:
1. **Create a new file**: In your repository, create a new file named `README.md`.
2. **Copy and paste the content**: Copy the content provided above and paste it into the `README.md` file.
3. **Customize the content**: Replace `https://github.com/yourusername/simple-keylogger.git` with the actual URL of your GitHub repository.
