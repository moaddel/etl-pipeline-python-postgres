import logging
from sqlalchemy import create_engine


def load_data(df, db_config):
    try:
        engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@"
            f"{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )

        df.to_sql(
            "employees",
            engine,
            if_exists="replace",
            index=False
        )

        logging.info("Data loaded into PostgreSQL successfully")

    except Exception as e:
        logging.error(f"Load error: {e}")
        raise