from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)               # __name__: predefined var, set to module name in which it it used.
app.config.from_object(Config)
db = SQLAlchemy(app)                # engine created.
migrate = Migrate(app, db)


from app import routes, models      # bottom import