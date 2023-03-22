from extension import db
import uuid

class Entry(db.Model):
    id = db.Column(db.String, primary_key=True,default=uuid.uuid4)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    how_did_you_hear = db.Column(db.String(100))
    competition_id = db.Column(db.String, db.ForeignKey('competition.id'), nullable=True)
    is_entrant_part_of_institution = db.Column(db.Boolean, default=False, nullable=False)
    i_am_part_of = db.Column(db.String, default=False, nullable=False)
    created_by = db.Column(db.String(100))
    updated_by = db.Column(db.String(100))
    is_delete = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    
    def __repr__(self):
        return f'<Entry {self.name}>'