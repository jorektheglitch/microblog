from flask import Flask

from app.auth import bp as auth_bp
from app.errors import bp as errs_bp
from app.main import bp as main_bp


def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(errs_bp)
    app.register_blueprint(main_bp)