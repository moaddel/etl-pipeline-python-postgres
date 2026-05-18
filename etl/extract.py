import pandas as pd
import logging


def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)

        logging.info("Data extracted successfully")

        return df

    except Exception as e:
        logging.error(f"Extract error: {e}")
        raise