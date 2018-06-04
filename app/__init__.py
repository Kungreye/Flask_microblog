from flask import Flask

app = Flask(__name__)   # __name__: python predefined var, set to module name in which it it used.

from app import routes  # bottom import; since routes(within app package) will import app variable defined here.