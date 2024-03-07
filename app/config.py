import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    ORGANIZATION_NAME = os.getenv('ORGANIZATION_NAME')
    GITHUB_P_ACCESSTOKEN = os.getenv('GITHUB_P_ACCESSTOKEN')
