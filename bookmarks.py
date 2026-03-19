import json
import os

FILE = "bookmarks.json"

def load():
    if not os.path.exists(FILE):
        return []

    data = json.load(open(FILE))

    fixed = []
    for item in data:
        if isinstance(item, str):
            fixed.append(item)
        elif isinstance(item, dict) and "url" in item:
            fixed.append(item["url"])

    return fixed

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add(url):
    data = load()
    if url not in data:
        data.append(url)
        save(data)

def get():
    return load()