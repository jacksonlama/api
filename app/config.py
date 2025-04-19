import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SCRAPE_HOUR = int(os.getenv("SCRAPE_HOUR", 0))  # 12:00 AM by default
    SCRAPE_MINUTE = int(os.getenv("SCRAPE_MINUTE", 0))
    DATA_DIR = os.getenv("DATA_DIR", "saved_data")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
