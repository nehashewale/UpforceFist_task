
from flask import Blueprint, request
from flask_restful import Api
from extension import db
from user.service import UserDAO
from user.utils import UserView
from utils import Resource, ok_response,error_response

user_blueprint = Blueprint('user', __name__)
user_api = Api(user_blueprint)

class User(Resource):
    """
        This is user class which is used to create, update and get users
    """
    def get(self, id=None):
        user_dao = UserDAO()
        user_view = UserView()
        if id:
            user = user_dao.get_user_by_id(id)
            if not user:
                return error_response(code=404, message="User Not found")
            response = user_view.create_single_user_reponse(user)
            return ok_response(response)
        
        params = request.args.to_dict()
        name = params.get("name", None)
        if name:
            user = user_dao.get_user_by_name(name) 
            if not user:
                return error_response(code=404, message="User Not found")
            response = user_view.create_single_user_reponse(user)
        else:
            users = user_dao.get_all_users()
            response = user_view.create_multiple_user_response(users)
        return ok_response(response)

    def post(self):
        body = request.get_json()
        user_dao = UserDAO()
        user_dao.create_user(body)
        return ok_response("User Created")

    def put(self, id):
        body = request.get_json()
        user_dao = UserDAO()
        user_dao.update_user_in_db(id, body)
        return ok_response("Updated")

user_api.add_resource(User, '/user', '/user/<id>')