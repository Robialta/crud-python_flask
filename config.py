import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'apalahdisinibisaapasajaasalkanjangakpakaispasi'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:root@localhost/kuliah'
    SQLALCHEMY_TRACK_MODIFICATION = True