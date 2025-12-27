from datetime import datetime
import json
from json import JSONDecodeError

FILE_NAME = "students.json"

def save_user_data(student):
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    try:
        with open(FILE_NAME, 'r') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, JSONDecodeError):
        data = {}

    data[timestamp] = student

    with open(FILE_NAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def load_user_data():
    try:
        with open(FILE_NAME, 'r') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, JSONDecodeError):
        return {}
