import os

WTF_CSRF_ENABLED = True
SECRET_KEY = '6454564HGLKSNHGKL69'

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = "mysql://Adora:62866181@ali@localhost:3306/cano"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True



