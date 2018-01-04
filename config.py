import os

WTF_CSRF_ENABLED = True
SECRET_KEY = '6454564HGLKSNHGKL69'

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = "mysql://User:Password@localhost:3306/database"
#note that mysql database should be created before running ./create_db.py

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True



