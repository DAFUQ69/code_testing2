import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test1:12345678@localhost/product_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
