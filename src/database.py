from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


MYSQL_DB_HOST = os.environ.get('MYSQL_DB_HOST','db')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_DB_PORT = os.environ.get('MYSQL_DB_PORT',3306)
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')

URL_DATABASE=f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DB_HOST}/{MYSQL_DATABASE}'

engine=create_engine(URL_DATABASE)

session_local =sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()