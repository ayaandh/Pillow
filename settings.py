import json
import os

FILE = "settings.json"

DEFAULT = {
    "homepage": "https://www.google.com"
}

def load():
    if os.path.exists(FILE):
        return json.load(open(FILE))
    return DEFAULT

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_homepage():
    return load().get("homepage", DEFAULT["homepage"])

def set_homepage(url):
    data = load()
    data["homepage"] = url
    save(data)