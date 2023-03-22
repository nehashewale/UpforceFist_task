

from competition.models import Competition
from extension import db
# DAO Data Access Object competition
class CompetitionDAO():
    def __init__(self) -> None:
        pass

    def get_competition_by_name(self, title):
        try:
            competition = Competition.query.filter_by(title=title).first() 
        except:
            competition = None
        return competition 

    def get_competition_by_id(self, id):
        try:
            competition = Competition.query.filter_by(id=id).first() 
        except:
            competition = None
        return competition 

    def get_all_competitions(self):
        try:
            competition = Competition.query.all() 
        except:
            competition = None
        return competition 

    def create_competition(self, competition_object):
        competition = Competition(**competition_object)
        db.session.add(competition)
        db.session.commit()
        return 

    def update_competition_in_db(self, id,body):
        try:
            competition = Competition.query.filter_by(id=id).first()
            competition.title = body.get('title','')
            competition.social_issue = body.get('social_issue')
            competition.user_id = body.get('user_id')
            competition.created_by = body.get('created_by','')
            competition.updated_by = body.get('updated_by','')
            competition.is_delete = body.get('is_delete',False)
            competition.is_active = body.get('is_active',True)
            db.session.commit()
            return True
        except:
            return False