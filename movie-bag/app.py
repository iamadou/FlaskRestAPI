#!/usr/bin/env python


from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_mail import Mail

from database.db import initialize_db

from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

mail = Mail(app)

# imports requiring app and mail
from resources.routes import initialize_routes
from resources.errors import errors
api = Api(app, errors=errors)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)
mail = Mail(app)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://localhost/movie-bag"}

initialize_db(app)

initialize_routes(api)

