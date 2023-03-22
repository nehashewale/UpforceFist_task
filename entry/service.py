
from entry.models import Entry
from extension import db
# DAO Data Access Object entry
class EntryDAO():
    def __init__(self) -> None:
        pass

    def get_entry_by_name(self, name):
        try:
            entry = Entry.query.filter_by(name=name).first() 
        except:
            entry = None
        return entry 

    def get_entry_by_id(self, id):
        try:
            entry = Entry.query.filter_by(id=id).first() 
        except:
            entry = None
        return entry 

    def get_all_entry(self):
        try:
            entry = Entry.query.all() 
        except:
            entry = None
        return entry 

    def create_entry(self, entry_object):
        entry = Entry(**entry_object)
        db.session.add(entry)
        db.session.commit()
        return 

    def update_entry_in_db(self, id,body):
        try:
            entry = Entry.query.filter_by(id=id).first()
            entry.name = body.get('name','')
            entry.country = body.get('country')
            entry.state = body.get('state')
            entry.how_did_you_hear = body.get('how_did_you_hear','')
            entry.Competition_id = body.get('Competition_id')
            entry.is_entrant_part_of_institution = body.get('is_entrant_part_of_institution', False)
            entry.i_am_part_of = body.get('i_am_part_of', '')
            entry.created_by = body.get('created_by','')
            entry.updated_by = body.get('updated_by','')
            entry.is_delete = body.get('is_delete',False)
            entry.is_active = body.get('is_active',True)
            db.session.commit()
            return True
        except:
            return False