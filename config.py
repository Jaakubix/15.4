import os

class Config:
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "change-me")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite"