from flask.json import jsonify
from app.repositories import userRepository
from flask_restful import Resource, marshal_with, fields, reqparse

resource_fields = {
    'id': fields.String,
    'email': fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('email')

class UserResource(Resource):

    @marshal_with(resource_fields)
    def get(self):
        users = userRepository.get_all_users_db()
        return (users)
    
    def post(self):
        args = parser.parse_args()
        emailInput = args['email']
        if userRepository.createUser(emailInput):
            return jsonify({"message": "User Created"})
        else:
            return jsonify({"message": "Error Creating User"})
        
