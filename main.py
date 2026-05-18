import logging

from etl.extract import extract_data
from etl.transform import clean_data, add_salary_level, validate_data
from etl.load import load_data
from config import DB_CONFIG


# =========================
# Logging Configuration
# =========================
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        logging.info("START ETL PIPELINE")

        # =========================
        # Extract
        # =========================
        df = extract_data("data/data.csv")
        logging.info("CSV loaded successfully")

        print("\nOriginal Data:\n", df)

        # =========================
        # Transform
        # =========================
        df = clean_data(df)
        df = add_salary_level(df)
        df = validate_data(df)

        logging.info("Data transformation completed")

        print("\nCleaned Data:\n", df)

        # =========================
        # Load
        # =========================
        load_data(df, DB_CONFIG)

        logging.info("Data loaded into PostgreSQL successfully ")
        logging.info("ETL PIPELINE FINISHED SUCCESSFULLY")

        print("\nETL PIPELINE COMPLETED SUCCESSFULLY ")

    except Exception as e:
        logging.error(f"ETL PIPELINE FAILED: {e}")
        print("ERROR:", e)


if __name__ == "__main__":
    main()