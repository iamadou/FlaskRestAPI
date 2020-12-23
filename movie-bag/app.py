#!/usr/bin/env python


from flask import Flask, jsonify, request


app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)
    
    
@app.route('/movies', methods=['POST'])
def add_movies():

    movie = request.get_json()
    print(movie)
    movies.append(movie)
    print(movies)
    return {'id': len(movies)}, 200


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    print(index)
    movie = request.get_json()
    print(request)
    print(movie)
    print(movies[index])
    movies[index] = movie
    print(movies[index])
    return jsonify(movies[index]), 200
    

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200



if __name__ == "__main__":
    app.run()
