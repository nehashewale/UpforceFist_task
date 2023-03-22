

class UserView():
    def create_single_user_reponse(self, user):
        user_response =  {
            "id" : user.id,
            "name" : user.name,
            "email" : user.email,
            "gender" : user.gender,
            "phone_number" : user.phone_number,
            "created_by" : user.created_by,
            "updated_by" : user.updated_by,
            "is_delete" : user.is_delete,
            "is_active" : user.is_active
            }
        return user_response

    def create_multiple_user_response(self,users):
        users_response = []
        for user in users:
            user_response = self.create_single_user_reponse(user)
            users_response.append(user_response)
        return users_response
