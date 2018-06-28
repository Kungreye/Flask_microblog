from flask import Blueprint


bp = Blueprint('auth', __name__)


from app.auth import routes

# app/auth: email & forms are not imported
# Since both do not need the above bp, so not registered by importing.