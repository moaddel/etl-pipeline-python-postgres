import pandas as pd
import config

def extract_data():
    return pd.read_csv(config.DATA_PATH)