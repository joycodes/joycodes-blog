from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

mail = Mail()


db = SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)
    
    #Initialising flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #Creating the app configurations
    app.config.from_object(config_options[config_name])
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    #registering  blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
    
    #configure UploadSet
    configure_uploads(app,photos)
    
    #settings config
    from .requests import configure_request
    configure_request(app)
    
    
    return app