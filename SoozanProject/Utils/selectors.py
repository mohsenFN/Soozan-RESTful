from User.models import User

class Selector:


    def user_instance(user_id):
        return User.objects.filter(id = user_id)