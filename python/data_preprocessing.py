# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_clean_data(file_path):
    """Load and preprocess dataset."""
    data = pd.read_csv(file_path)
    # Example cleaning step: Drop rows with missing values
    data = data.dropna()
    return data

def split_data(data, test_size=0.2):
    """Split data into training and testing sets."""
    return train_test_split(data, test_size=test_size, random_state=42)

if __name__ == "__main__":
    print("This module preprocesses the data.")
