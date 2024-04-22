import logging
import psycopg2
from contextlib import contextmanager
from dotenv import dotenv_values

config = dotenv_values('.env')

#Get data from .env file. You need to create env file with data in .env-example
@contextmanager
def connect():
    try:    
        conn = psycopg2.connect(host=config['PG__HOST'],database=config['PG__DB'],user=config['PG__USER'],password=config['PG__PASSWORD'],)
        try:
            yield conn
        finally:
            conn.close()
    except psycopg2.OperationalError as e:
        logging.error(e)