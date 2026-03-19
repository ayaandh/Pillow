import json
import os

FILE = "passwords.json"

def load_passwords():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_passwords(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_password(site, username, password):
    data = load_passwords()
    data[site] = {"username": username, "password": password}
    save_passwords(data)

def get_password(site):
    data = load_passwords()
    return data.get(site)

def get_all():
    return load_passwords()