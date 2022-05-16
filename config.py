import os

class Config:
    '''
    general configuration parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    
    #email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'


    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    '''
    production configuration subclass
    Args:
        Config: The general configuration class with the the general configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joyce:root@localhost/joycodesblog'
    DATABASE_URL = 'postgres://socruucrygsxud:b2958f9f725ee4618c6ce64d3f9bd2567137f6ba0e68de9684a6240d2cc1f275@ec2-3-229-11-55.compute-1.amazonaws.com:5432/depopniuuokdgm'
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
    