import pandas as pd
import logging
from sqlalchemy import create_engine
from config import DB_CONFIG

# ======================
# Logging setup
# ======================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("START ETL")

# ======================
# Extract
# ======================
try:
    df = pd.read_csv("data/data.csv")
    logging.info("CSV loaded successfully")
except Exception as e:
    logging.error(f"Error reading CSV: {e}")
    raise

# ======================
# Transform
# ======================
try:
    # Drop missing values
    df = df.dropna()

    # Convert types safely
    df.loc[:, "age"] = df["age"].astype(int)
    df.loc[:, "salary"] = df["salary"].astype(int)

    # Create salary level feature
    def salary_level(x):
        if x > 7000:
            return "high"
        else:
            return "medium"

    df.loc[:, "salary_level"] = df["salary"].apply(salary_level)

    logging.info("Data transformation completed")

    print("\nCleaned Data:")
    print(df)

except Exception as e:
    logging.error(f"Error in transformation: {e}")
    raise

# ======================
# Load
# ======================
try:
    engine = create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    df.to_sql("employees", engine, if_exists="replace", index=False)

    logging.info("Data loaded into PostgreSQL successfully 🚀")

except Exception as e:
    logging.error(f"Database error: {e}")
    raise

logging.info("ETL PIPELINE FINISHED SUCCESSFULLY")