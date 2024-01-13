from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

connection = psycopg2.connect(database=os.environ["DB"],
                              host=os.environ["DB_HOST"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASSWORD"],
                              port=os.environ["DB_PORT"])
