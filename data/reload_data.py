import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# mysql connection
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)

def reload():
    df = pd.read_csv("data/online_shoppers_intention.csv")

    df.to_sql(
        "online_shoppers",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully!")

reload()