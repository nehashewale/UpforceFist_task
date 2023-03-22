
from sqlalchemy.dialects.postgresql import ARRAY
from extension import db
import uuid

class Competition(db.Model):
    id = db.Column(db.String, primary_key=True,default=uuid.uuid4)
    title = db.Column(db.String(100))
    social_issue = db.Column(ARRAY(db.String),nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=True)
    created_by = db.Column(db.String(100))
    updated_by = db.Column(db.String(100))
    is_delete = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    

