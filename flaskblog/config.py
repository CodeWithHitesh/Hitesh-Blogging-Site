import os


class Config:
    SECRET_KEY = str(os.environ.get("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = str(os.environ.get("SQLALCHEMY_DATABASE_URI"))
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = str(os.environ.get("EMAIL_USERNAME"))
    # App Password.
    MAIL_PASSWORD = str(os.environ.get("EMAIL_PASS"))
