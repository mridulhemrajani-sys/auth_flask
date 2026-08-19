from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from app import app
from datetime import datetime
# import config

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return print(f'ID : {self.id}, Name : {self.name}, Email ID ; {self.email}')
