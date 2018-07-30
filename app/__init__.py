# -*- encoding: utf-8 -*-
"""
Initalize your flask app
"""
from flask import Flask
# from app.database import db_session


def create_app(test_config=None):
    """ Create and configure the app """
    app = Flask(__name__, instance_relative_config=True)

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # Initalize database
    from app.database import init_db

    init_db()

    # Initialize routes
    from app.main_page import main_page

    app.register_blueprint(main_page)


    return app


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()