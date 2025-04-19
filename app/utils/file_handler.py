import os
import json
from datetime import datetime

def get_data_path(api_name: str) -> str:
    date_str = datetime.now().strftime('%Y-%m-%d')
    return f"saved_data/{api_name}/{date_str}.json"

def data_exists(api_name: str) -> bool:
    return os.path.exists(get_data_path(api_name))

def save_data(api_name: str, data: dict):
    path = get_data_path(api_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_data(api_name: str) -> dict:
    with open(get_data_path(api_name)) as f:
        return json.load(f)
