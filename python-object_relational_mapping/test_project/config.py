# config.py
import os

DB_USER = os.getenv("DB_USER", "emerson_dev")
DB_PASSWORD = os.getenv("DB_PASSWORD", "P8796")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "tracker_db")

DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"