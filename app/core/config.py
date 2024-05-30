import os

class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://hanslab.org:57017/")

settings = Settings()