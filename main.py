from etl.extract import extract_data
from etl.transform import clean_data, add_salary_level
from etl.load import load_data

print("START ETL")

# EXTRACT
df = extract_data()
print("Extract done")

# TRANSFORM
df = clean_data(df)
df = add_salary_level(df)
print("Transform done")

# LOAD
load_data(df)
print("Load done 🚀")

print("DONE SUCCESSFULLY")