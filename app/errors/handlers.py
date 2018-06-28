from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()       # to ensure failed db sessions don't interfere with db accesses triggered by template. Rollback to set the session to a clean state.
    return render_template('errors/500.html'), 500