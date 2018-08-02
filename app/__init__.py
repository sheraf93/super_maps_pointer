# -*- encoding: utf-8 -*-
"""
Initalize your flask app
"""
from flask import Flask


def create_app():
    """ Create and configure the app """
    app = Flask(__name__)

    # Initialize database
    from app.database import db_session, init_db

    init_db()

    # Flask will automatically remove database sessions at the end of the request or when the application shuts down
    # See http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/#declarative
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Initialize routes
    from app.main_page import main_page

    app.register_blueprint(main_page)

    return app
