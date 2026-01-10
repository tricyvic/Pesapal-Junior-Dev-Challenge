import json
import os

DATA_DIR = "data"

def save_table(table):
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, f"{table.name}.json")
    with open(filepath, "w") as f:
        json.dump(list(table.rows.values()), f, indent=2)

def load_table(name):
    filepath = os.path.join(DATA_DIR, f"{name}.json")
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)
