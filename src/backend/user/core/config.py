from datetime import timedelta
from os import getenv as env

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = env("DB_LINK")

SECRET_KEY = env("SECRET_KEY")
ALGORITHM = env("ALGORITHM")

ACCESS_EXPIRES_TIME = timedelta(hours=8)
REFRESH_EXPIRES_TIME = timedelta(days=7)
