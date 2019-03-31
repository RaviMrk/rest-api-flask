import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
   
    parser.add_argument('caste',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('fname',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('lname',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('gender',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('university',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('tfws',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('defence',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    parser.add_argument('department',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('merit',
        type=int,
        required=True,
        help="This field cannot be blank."
    )



    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class UserList(Resource):
    @jwt_required()
    def get(self,username):
        userdata = UserModel.find_by_username(username)
        if(userdata):
            return userdata.json()
        return {'message' : 'invalid credentials'} ,400
            
            

        
        #return {"user":[x.json() for x in UserModel.query.all()]}
        
