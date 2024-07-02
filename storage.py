import json

def save_to_file(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump([item.to_dict() for item in data], f, indent=4)
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_from_file(filename, cls):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [cls(**item) for item in data]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading from file: {e}")
        return []
