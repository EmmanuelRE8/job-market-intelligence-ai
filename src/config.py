from dotenv import load_dotenv
import os

load_dotenv()

LINKEDIN_API_KEY = os.getenv("LINKEDIN_API_KEY")

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

ENVIRONMENT = os.getenv("ENVIRONMENT")