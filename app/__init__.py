from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config


app = Flask(__name__)               # __name__: predefined var, set to module name in which it it used.
app.config.from_object(Config)

db = SQLAlchemy(app)                # engine created.
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'  # force user to login by redirect to view func 'login'.


from app import routes, models      # bottom imports