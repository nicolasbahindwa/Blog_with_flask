import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
from blog_with_flask.Config import Config

load_dotenv()
# from flask_mail import Mail
# from smtpapi import SMTPAPIHeader
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


# app.config['SECRET_KEY']='6056863be7cd5b43c163a7b3bde8397ae220d420da51e4e86b8e40107f84640e'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///F:\\BLOG_WITH_FLASK\\site.db'
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
 
key = os.getenv('apikey')
 




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    

    from blog_with_flask.users.routes import users
    from blog_with_flask.posts.routes import posts
    from blog_with_flask.main.routes import main
    from blog_with_flask.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app