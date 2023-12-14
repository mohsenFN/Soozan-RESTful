from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, number, password, **extra_fields):
       
        if not number:
            raise ValueError("The Phone Number must be set")
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save()
        return user