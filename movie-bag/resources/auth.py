#!/usr/bin/env python


from flask import request, Response
from database.models import User
from flask_restful import Resource



class SignupApi(Resource):

    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
        
    def get(self):
        user = User.objects().to_json()
        return Response(user, mimetype="application/json", status=200)
    
