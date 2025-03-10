# storage.py (JSON Storage Management)
import json
import os

def load_data(file):
    """Load data from a JSON file. if file doesn't exist, return an emtpy dictionary."""
    if not os.path.exists(file):
        return {}
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except(json.JSONDecodeError, FileNotFoundError):
        return {}


def save_data(file, data):
    """Save data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)