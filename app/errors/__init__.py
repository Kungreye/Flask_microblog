from flask import Blueprint


bp = Blueprint('errors', __name__)  # (name, import_name) , import_name is base_module, typically set to __name__.

from app.errors import handlers     # bottom import to avoid circular dependencies.

# After blueprint obj is created, import the handlers.py module.
# So that error handlers in it are registered with the blueprint.