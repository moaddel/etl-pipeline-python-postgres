from sqlalchemy import create_engine
import config

def load_data(df):
    engine = create_engine(
        f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}"
        f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )

    df.to_sql(
        config.TABLE_NAME,
        engine,
        if_exists="replace",
        index=False
    )