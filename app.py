import os
from flask_smorest import Api
from flask import Flask, request, jsonify
# from db import stores, items
# from flask_smorest import abort

from db import db
import models

from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

# to implement the API factory pattern we need to create a function that will return the app instance


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
    #     "DATABASE_URL", "sqlite:///data.db")
    # create mysql database
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        'DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/stores_db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    # Create all tables in the database before starting the server
    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app
