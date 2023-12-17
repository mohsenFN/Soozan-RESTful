from User.models import User

class UserSelector:


    def user_instance(user_id):
        return User.objects.get(id = user_id)

    def user_is_artist(number):
        if not User.objects.filter(number=number).exists():
            raise User.DoesNotExist

        if User.objects.filter(number=number)[0].user_type == 'ARTIST':
            return True

        return False


    def user_is_applicant(number):
        if not User.objects.filter(number=number).exists():
            raise User.DoesNotExist

        if User.objects.filter(number=number)[0].user_type == 'USER':
            return True
            
        return False
        
    
    
