import os

class Config:
    # Basic Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-string'
    
    # SQLAlchemy Configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    
    # The key to cross-container communication:
    # The host is the name of the PostgreSQL service in your docker-compose file.
    # The default PostgreSQL port is 5432.
    DB_USER = os.environ.get('POSTGRES_USER') or 'datingapp_user'
    DB_PASS = os.environ.get('POSTGRES_PASSWORD') or 'supersecurepass'
    DB_NAME = os.environ.get('POSTGRES_DB') or 'datingapp_db'
    DB_HOST = os.environ.get('POSTGRES_HOST') or 'postgres_db' # <--- USE THE SERVICE NAME!
    
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )

class TestingConfig(Config):
    TESTING = True
    # Use a separate database for testing (e.g., an in-memory SQLite for speed)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'