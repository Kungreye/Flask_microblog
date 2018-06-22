import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from config import Config


app = Flask(__name__)               # __name__: predefined var, set to module name in which it it used.
app.config.from_object(Config)
db = SQLAlchemy(app)                # engine created.
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'  # force user to login by redirect to view func 'login'.
login.login_message = _l('Please log in to access this page.')  # override default message, ensure flashed message during redirect can also be translated.
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)


if not app.debug:                   # only for debug mode: off
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()     # only be used when credentials are supplied.
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr= 'no-reply@' + app.config['MAIL_SERVER'],
            toaddrs= app.config['ADMINS'],
            subject= 'Microblog Failure',
            credentials= auth,
            secure= secure,)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)     # app.logger object is from Flask.

    if not os.path.exists('logs'):              # if Microblog/logs/ exists or not
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))        
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')



@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES']) # compare list of langs requested by client against the supported langs of app, return best choice.
# Decorated func is invoked for each request to select a translation to use for that request.

from app import routes, models, errors      # bottom imports