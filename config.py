import os
class Config:
    '''
    general configuration parent class
    '''
    #email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://apkorittdnfgzp:b1ffa862052bfe1421c3e537a6f196405b12f46d102389fa6ee941187882916a@ec2-50-16-221-180.compute-1.amazonaws.com:5432/d91vs7aqj34kv6'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    '''
    production configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://joyce:root@localhost/joycodesblog'
class DevConfig(Config):
    '''
    development configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
    