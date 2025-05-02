import json
import threading
from pathlib import Path

DATA_FILE = Path('data/user_data.json')
storage_lock = threading.Lock()

def load_user_data():
    if DATA_FILE.exists():
        with DATA_FILE.open('r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_user_data(data):
    with storage_lock:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with DATA_FILE.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def set_user_scores(user_id, scores):
    data = load_user_data()
    data.setdefault(str(user_id), {})['scores'] = scores
    save_user_data(data)

def get_user_scores(user_id):
    data = load_user_data()
    return data.get(str(user_id), {}).get('scores')
