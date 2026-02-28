import os 
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SERP_API_KEY = os.getenv("SERPAPI_API_KEY")


    MODEL_NAME = 'gemini-3-flash-preview'
    TEMPERATURE = 0
    MAX_ITERATIONS = 3

settings = Settings()
