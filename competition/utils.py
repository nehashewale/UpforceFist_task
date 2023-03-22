

class CompetitionView():
    def create_single_competition_reponse(self, competition):
        competition_response =  {
            "id" : competition.id,
            "title" : competition.title,
            "social_issue" : competition.social_issue,
            "user_id" : competition.user_id,
            "created_by" : competition.created_by,
            "updated_by" : competition.updated_by,
            "is_delete" : competition.is_delete,
            "is_active" : competition.is_active
            }
        return competition_response

    def create_multiple_competition_response(self,competitions):
        competitions_response = []
        for competition in competitions:
            competition_response = self.create_single_competition_reponse(competition)
            competitions_response.append(competition_response)
        return competitions_response
