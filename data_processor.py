import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error loading dataset: {str(e)}")

def clean_data(df):
    # Basic cleaning: remove empty rows, normalize text
    df = df.dropna(how='all')
    df = df.apply(lambda x: x.str.lower().str.strip() if x.dtype == "object" else x)
    return df