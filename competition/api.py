
from flask import Blueprint, request
from flask_restful import Api
from extension import db
from competition.service import CompetitionDAO
from competition.utils import CompetitionView
from utils import Resource, ok_response,error_response

competition_blueprint = Blueprint('competition', __name__)
competition_api = Api(competition_blueprint)

class Competition(Resource):
    def get(self, id=None):
        competition_dao = CompetitionDAO()
        competition_view = CompetitionView()
        if id:
            competition = competition_dao.get_competition_by_id(id)
            if not competition:
                return error_response(code=404, message="competition Not found")
            response = competition_view.create_single_competition_reponse(competition)
            return ok_response(response)
        
        params = request.args.to_dict()
        title = params.get("title", None)
        if title:
            competition = competition_dao.get_competition_by_name(title) 
            if not competition:
                return error_response(code=404, message="competition Not found")
            response = competition_view.create_single_competition_reponse(competition)
        else:
            competitions = competition_dao.get_all_competitions()
            response = competition_view.create_multiple_competition_response(competitions)
        return ok_response(response)

    def post(self):
        body = request.get_json()
        competition_dao = CompetitionDAO()
        competition_dao.create_competition(body)
        return ok_response("competition Created")

    def put(self, id):
        body = request.get_json()
        competition_dao = CompetitionDAO()
        competition_dao.update_competition_in_db(id, body)
        return ok_response("Updated")

competition_api.add_resource(Competition, '/competition', '/competition/<id>')