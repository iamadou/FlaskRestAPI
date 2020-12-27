#!/usr/bin/env python


from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes



app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)


app.config["MONGODB_SETTINGS"] = {"host": "mongodb://localhost/movie-bag"}

initialize_db(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run()
