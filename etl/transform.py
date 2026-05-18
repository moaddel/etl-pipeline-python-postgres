import logging


def clean_data(df):
    try:
        df = df.dropna().copy()

        df["age"] = df["age"].astype(int)
        df["salary"] = df["salary"].astype(int)

        logging.info("Data cleaning completed successfully")
        return df

    except Exception as e:
        logging.error(f"Error in clean_data: {e}")
        raise


def add_salary_level(df):
    try:
        df["salary_level"] = df["salary"].apply(
            lambda x: "high" if x > 7000 else "medium"
        )

        logging.info("Feature engineering (salary_level) added successfully")
        return df

    except Exception as e:
        logging.error(f"Error in add_salary_level: {e}")
        raise


def validate_data(df):
    try:
        # Missing values check
        if df.isnull().sum().sum() > 0:
            logging.warning("Dataset contains missing values")

        # Negative salary check
        if (df["salary"] < 0).any():
            raise ValueError("Salary cannot be negative")

        # Negative age check
        if (df["age"] < 0).any():
            raise ValueError("Age cannot be negative")

        logging.info("Data validation passed successfully")
        return df

    except Exception as e:
        logging.error(f"Validation error: {e}")
        raise