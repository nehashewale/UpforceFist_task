
from user.models import User
from extension import db
from user.utils import UserView

# DAO Data Access Object
class UserDAO():
    def __init__(self) -> None:
        self.user = None
        pass

    def get_user_by_name(self, name):
        try:
            user = User.query.filter_by(name=name).first() 
        except:
            user = None
        return user 

    def get_user_by_id(self, id):
        try:
            user = User.query.filter_by(id=id).first() 
        except:
            user = None
        return user 

    def get_all_users(self):
        try:
            user = User.query.all() 
        except:
            user = None
        return user 

    def create_user(self, user_object):
        user = User(**user_object)
        db.session.add(user)
        db.session.commit()
        return 

    def update_user_in_db(self, id,body):
        try:
            user = User.query.filter_by(id=id).first()
            user.name = body.get('name','')
            user.email = body.get('email','')
            user.gender = body.get('gender','')
            user.phone_number = body.get('phone_number','')
            user.created_by = body.get('created_by','')
            user.updated_by = body.get('updated_by','')
            user.is_delete = body.get('is_delete',False)
            user.is_active = body.get('is_active',True)
            db.session.commit()
            return True
        except:
            return False
