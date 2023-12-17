from User.models import User

class Selector:


    def user_instance(user_id):
        return User.objects.get(id = user_id)