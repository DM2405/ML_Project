# This file loads transformed data into PostgreSQL data warehouse

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

def get_mysql_engine():
    # build mysql connection string for source database
    url = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{quote_plus(os.getenv('DB_PASSWORD'))}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    print(url)  # temporary debug

    return create_engine(url)

def get_pg_engine():
    # build postgresql connection string for data warehouse
    url = (
        f"postgresql+psycopg2://{os.getenv('PG_USER')}:{quote_plus(os.getenv('PG_PASSWORD'))}"
        f"@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{quote_plus(os.getenv('PG_NAME'))}"
    )

    print(url)  # temporary debug

    return create_engine(url)

def load_data(df):
    # load transformed data into postgresql warehouse
    pg_engine = get_pg_engine()

    df.to_sql(
        'transformed_shoppers',
        pg_engine,
        if_exists='replace',
        index=False
    )

    print(f"Loaded {len(df)} rows into PostgreSQL warehouse")

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    df = extract_data()
    df = transform_data(df)
    load_data(df)