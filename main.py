import pandas as pd
from sqlalchemy import create_engine

# STEP 1: EXTRACT
csv_path = r"d:\DOCUMENT\Associate_Details.xlsx"

df = pd.read_excel(csv_path)

print("Data preview:")
print(df.head())
print("Raw length:", len(df))

# STEP 2: TRANSFORM
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Only drop rows where all cells are blank
df = df.dropna(how="all")

print("Length after dropna(how='all'):", len(df))

# STEP 3: LOAD
engine = create_engine("postgresql+psycopg2://username:password@host:port/database")

df.to_sql("my_table", con=engine, if_exists="replace", index=False)

print("ETL pipeline completed successfully!")
