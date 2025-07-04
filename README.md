# ETL Pipeline

This project is an **ETL (Extract, Transform, Load) pipeline** built with Python.  
It reads data from an Excel file, performs cleaning, and loads the results into a PostgreSQL database.

---


## ⚙️ Requirements

- Python 3.7+
- PostgreSQL
- Python packages:
  - pandas
  - SQLAlchemy
  - psycopg2-binary

Install dependencies with:

```bash
pip install pandas sqlalchemy psycopg2-binary
```

🧹 What This ETL Does

✅ Extract

Reads an Excel file using pandas.

✅ Transform

Normalizes column names (lowercase, underscores).

Drops completely blank rows.

✅ Load

Inserts data into PostgreSQL.

