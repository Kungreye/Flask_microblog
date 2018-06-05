from flask import Flask
from config import Config

app = Flask(__name__)   # __name__: predefined var, set to module name in which it it used.
app.config.from_object(Config)

from app import routes  # bottom import; since routes(within app package) will import app variable defined here.