from flask import request, Response
from database.models import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class MoviesApi(Resource):
    
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)
        
    @jwt_required
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {"id": str(id)}, 200

class MovieApi(Resource):
    
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return "", 200
    @jwt_required
    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return "", 200
    
    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype="application/json", status=200)   
         

"""
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
    
"""