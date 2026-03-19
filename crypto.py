from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def get_key():
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def encrypt(text):
    f = Fernet(get_key())
    return f.encrypt(text.encode()).decode()

def decrypt(text):
    f = Fernet(get_key())
    return f.decrypt(text.encode()).decode()