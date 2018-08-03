# -*- encoding: utf-8 -*-
"""
Initalize your flask app
"""
import os
from flask import Flask
from flask_cors import CORS


def create_app():
    """ Create and configure the app """
    app = Flask(__name__)
    CORS(app)

    # Initialize database
    from app.database import db_session, init_db

    init_db()

    # Flask will automatically remove database sessions at the end
    # See http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/#declarative
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Initialize routes
    from app.main_page import main_page

    app.register_blueprint(main_page)

    # Support debug with VSCODE
    if app.debug:
        import ptvsd

        ptvsd.enable_attach(os.getenv('SECRET_DEBUG'),
                            address=('0.0.0.0', 3000))

    return app
