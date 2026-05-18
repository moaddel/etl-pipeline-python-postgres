def clean_data(df):
    df = df.dropna().copy()

    df.loc[:, "age"] = df["age"].astype(int)
    df.loc[:, "salary"] = df["salary"].astype(int)

    return df


def add_salary_level(df):
    df = df.copy()

    df.loc[:, "salary_level"] = df["salary"].apply(
        lambda x: "high" if x > 7000 else "medium"
    )

    return df