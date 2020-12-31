import unittest
import json

from tests.BaseCase import BaseCase

class TestGetMovies(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/movies')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_movie_response(self):
        # Given
        name = "Paura Kh"
        email = "paurakh011@gmail.com"
        password = "mycoolpassword"
        user_payload = json.dumps({
            "name": name,
            "email": email,
            "password": password
        })

        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        movie_payload = {
            "name": "Star Wars: The Rise of Skywalker",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        }
        response = self.app.post('/api/movies',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(movie_payload))
        response_id = response.json['id']

        # When
        response = self.app.get('/api/movies/'+str(response_id))
        added_movie = response.json["_id"]["$oid"]

        # Then
        self.assertEqual(response_id, added_movie)
        self.assertEqual(200, response.status_code)
