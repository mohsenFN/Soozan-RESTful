

class UserValidator:

    valid_user_types = ['ARTIST', 'USER']


    def __init__(self, validated_data):
        self.number = validated_data.get('number')
        self.password = validated_data.get('password')
        self.user_type = validated_data.get('user_type')


    def check_number(self):
        if len(self.number) == 11 and self.number.isnumeric():
            return True
        
        return False


    def check_password(self):
        if len(self.password) < 8:
            return False
        return True


    def check_user_type(self):
        if self.user_type not in self.valid_user_types:
            return False
        return True

    


        