#!/usr/bin/env python

from werkzeug.exceptions import HTTPException



class InternalServerError(HTTPException):
    code = 500

class SchemaValidationError(HTTPException):
    code = 400

class MovieAlreadyExistsError(HTTPException):
    code = 400

class UpdatingMovieError(HTTPException):
    code = 403

class DeletingMovieError(HTTPException):
    code = 403

class MovieNotExistsError(HTTPException):
    code = 400

class EmailAlreadyExistsError(HTTPException):
    code = 400

class UnauthorizedError(HTTPException):
    code = 401


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "MovieAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "MovieNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}
