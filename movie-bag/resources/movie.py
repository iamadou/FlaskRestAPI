from flask import Blueprint, request, Response
from database.models import Movie
import json


movies = Blueprint("movies", __name__)


@movies.route("/movies")
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@movies.route("/movies/<id>")
def get_movie(id):
    movie = Movie.objects.get(id=id).to_json()
    return Response(movie, mimetype="application/json", status=200)


@movies.route("/movies", methods=["POST"])
def add_movies():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {"id": str(id)}, 200


@movies.route("/movies/<id>", methods=["PUT"])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return "", 200


@movies.route("/movies/<id>", methods=["DELETE"])
def delete_movie(id):
    movie = Movie.objects.get(id=id).delete()
    return "", 200
