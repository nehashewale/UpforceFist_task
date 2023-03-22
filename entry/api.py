
from flask import Blueprint, request
from flask_restful import Api
from extension import db
from entry.service import EntryDAO
from entry.utils import EntryView
from utils import Resource, ok_response,error_response

entry_blueprint = Blueprint('entry', __name__)
entry_api = Api(entry_blueprint)

class entry(Resource):
    def get(self, id=None):
        entry_dao = EntryDAO()
        entry_view = EntryView()
        if id:
            entry = entry_dao.get_entry_by_id(id)
            if not entry:
                return error_response(code=404, message="entry Not found")
            response = entry_view.create_single_entry_reponse(entry)
            return ok_response(response)
        
        params = request.args.to_dict()
        name = params.get("name", None)
        if name:
            entry = entry_dao.get_entry_by_name(name) 
            if not entry:
                return error_response(code=404, message="entry Not found")
            response = entry_view.create_single_entry_reponse(entry)
        else:
            entrys = entry_dao.get_all_entry()
            response = entry_view.create_multiple_entry_response(entrys)
        return ok_response(response)

    def post(self):
        body = request.get_json()
        entry_dao = EntryDAO()
        entry_dao.create_entry(body)
        return ok_response("entry Created")

    def put(self, id):
        body = request.get_json()
        entry_dao = EntryDAO()
        entry_dao.update_entry_in_db(id, body)
        return ok_response("Updated")

entry_api.add_resource(entry, '/entry', '/entry/<id>')