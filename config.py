# from app import app
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.getenv('SECRET_KEY')

# import os

# class Config:
#     SECRET_KEY = '5cedb07260ddb9cf449221ec87021d1b77436a91194416ddfac0d7ebe179a71a'

# class Development:
#     SQLALCHEMY_DATABSE_URI = "postgresql://mridul:password@localhost:5432/flask"
#     DEBUG = True