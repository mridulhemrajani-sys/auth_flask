# from app import app
import os
from dotenv import load_dotenv
from datetime import timedelta
from flask_jwt_extended import JWTManager

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_VERIFY_SUB = False

jwt = JWTManager()
# import os

# class Config:
#     SECRET_KEY = '5cedb07260ddb9cf449221ec87021d1b77436a91194416ddfac0d7ebe179a71a'

# class Development:
#     SQLALCHEMY_DATABSE_URI = "postgresql://mridul:password@localhost:5432/flask"
#     DEBUG = True