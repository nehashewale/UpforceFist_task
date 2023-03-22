# id (uuid4 pk)
# name
# email
from extension import db
import uuid

class User(db.Model):
    id = db.Column(db.String, primary_key=True,default=uuid.uuid4)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    phone_number = db .Column(db.String(50)) 
    created_by = db.Column(db.String(100))
    updated_by = db.Column(db.String(100))
    is_delete = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
