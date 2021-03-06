import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, UserList
#from resources.item import Item, ItemList
#from resources.store import Store, StoreList
from flask_cors import CORS, cross_origin
from resources.clg import CollegeData

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'rk'
CORS(app)

api = Api(app)

                    #Request handling

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserList ,'/userdata/<string:username>')   #url/userdata
api.add_resource(CollegeData ,'/collegedata')               #url/collegedata
api.add_resource(UserRegister, '/register')                 #url/register

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
