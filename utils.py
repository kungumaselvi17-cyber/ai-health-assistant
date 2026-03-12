import os
from datetime import datetime
import json

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def create_upload_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created upload folder: {folder_path}")

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else ''

def format_timestamp(timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def validate_message(message):
    if not message or not isinstance(message, str):
        return False, "Message must be a non-empty string"

    if len(message.strip()) == 0:
        return False, "Message cannot be empty"

    if len(message) > 5000:
        return False, "Message is too long (max 5000 characters)"

    return True, "Valid message"

def format_response(success, data=None, error=None):
    response = {
        'success': success,
        'timestamp': format_timestamp()
    }

    if success and data is not None:
        response['data'] = data
    elif not success and error is not None:
        response['error'] = error

    return response

def log_message(message, level='INFO'):
    timestamp = format_timestamp()
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)
    return log_entry

def parse_medical_dosage(text):
    dosage_info = {
        'amount': None,
        'frequency': None,
        'duration': None
    }

    import re

    amount_pattern = r'(\d+)\s*(mg|ml|tablet|capsule)'
    amount_match = re.search(amount_pattern, text.lower())
    if amount_match:
        dosage_info['amount'] = f"{amount_match.group(1)} {amount_match.group(2)}"

    frequency_patterns = [
        r'(\d+)\s*time[s]?\s*(?:a|per)\s*day',
        r'once\s*daily',
        r'twice\s*daily',
        r'three\s*times\s*daily'
    ]
    for pattern in frequency_patterns:
        freq_match = re.search(pattern, text.lower())
        if freq_match:
            dosage_info['frequency'] = freq_match.group(0)
            break

    duration_pattern = r'(?:for\s*)?(\d+)\s*(day|week|month)'
    duration_match = re.search(duration_pattern, text.lower())
    if duration_match:
        dosage_info['duration'] = f"{duration_match.group(1)} {duration_match.group(2)}s"

    return dosage_info

def clean_medical_text(text):
    import re

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(r'[^\w\s.,;:()\-/]', '', text)

    text = text.strip()

    return text

def create_data_folder(folder_path='data'):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created data folder: {folder_path}")

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False

def load_from_json(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None
