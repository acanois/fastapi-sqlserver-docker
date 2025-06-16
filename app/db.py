"""DATABASE Connection"""

import os
import urllib

from sqlmodel import SQLModel, Session, create_engine
from tenacity import retry, stop_after_attempt, wait_fixed

from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.environ["DB_SERVER"]
DB_NAME = os.environ["DB_NAME"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

DRIVER_17 = "ODBC Driver 17 for SQL Server"
DRIVER_ENCODED_17 = urllib.parse.quote_plus(DRIVER_17)

CONNECTION_STRING = f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:1433/{DB_NAME}?driver={DRIVER_ENCODED_17}"

engine = create_engine(CONNECTION_STRING, echo=True)


def get_session():
    """Yields a session object for a database transaction"""
    with Session(engine) as session:
        yield session
