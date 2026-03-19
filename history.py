import json
import os

FILE = "history.json"

def load():
    if os.path.exists(FILE):
        return json.load(open(FILE))
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add(url):
    data = load()
    if url not in data:
        data.append(url)
        save(data)

def search(query):
    data = load()

    if not query:
        return data

    return [x for x in data if query.lower() in x.lower()]