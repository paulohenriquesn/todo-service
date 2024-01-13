from dotenv import load_dotenv
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

connection = psycopg2.connect(database=os.environ["DB"],
                              host=os.environ["DB_HOST"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASSWORD"],
                              port=os.environ["DB_PORT"])

url = URL.create(
    drivername="postgresql",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    database=os.environ["DB"]
)

engine = create_engine(url)
