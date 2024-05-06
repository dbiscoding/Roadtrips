class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///trips.db'
    SECRET_KEY = '$2b$12$1'
    GOOGLE_MAPS_API_KEY = 'AIzaSyD8Zf42FK8P_p3WLwwNoqeEH7-a7XRlNqk'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/trips'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
