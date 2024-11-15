# utils.py
import json

def read_config(config_path):
    """Read JSON configuration file."""
    with open(config_path, 'r') as file:
        return json.load(file)

def save_model(model, path):
    """Save a model to a file."""
    with open(path, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    print("Utility functions module.")
