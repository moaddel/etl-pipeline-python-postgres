# ETL Pipeline using Python and PostgreSQL

## Project Overview
This project is a simple ETL (Extract, Transform, Load) pipeline built with Python, Pandas, and PostgreSQL.

It reads data from a CSV file, cleans and transforms it, and loads it into a PostgreSQL database.

##  Tech Stack
- Python
- Pandas
- SQLAlchemy
- PostgreSQL

## ETL Process
1. **Extract**: Read data from CSV file
2. **Transform**:
   - Handle missing values
   - Convert data types
   - Create salary_level column
3. **Load**: Insert cleaned data into PostgreSQL database

##  Dataset
The dataset contains employee information:
- id
- name
- age
- salary

##  How to Run

Install dependencies:
```bash
pip install -r requirements.txt