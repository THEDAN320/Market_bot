"""module for configuration data."""
import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get("TOKEN")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
USERNAME = os.environ.get("USERNAME")
EMAIL = os.environ.get("EMAIL")
OPERATORS = os.environ.get("OPERATORS")
