from .base import *
from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")

DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
