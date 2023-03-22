

class EntryView():
    def create_single_entry_reponse(self, entry):
        entry_response =  {
            "id" : entry.id,
            "name" : entry.name,
            "country" : entry.country,
            "state" : entry.state,
            "how_did_you_hear" : entry.how_did_you_hear,
            "is_entrant_part_of_institution" : entry.is_entrant_part_of_institution,
            "i_am_part_of" : entry.i_am_part_of,
            "competition_id" : entry.competition_id,
            "created_by" : entry.created_by,
            "updated_by" : entry.updated_by,
            "is_delete" : entry.is_delete,
            "is_active" : entry.is_active
            }
        return entry_response

    def create_multiple_entry_response(self,entrys):
        entrys_response = []
        for entry in entrys:
            entry_response = self.create_single_entry_reponse(entry)
            entrys_response.append(entry_response)
        return entrys_response
