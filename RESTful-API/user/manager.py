from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, number, password, **kwargs):
       
        if not number:
            raise ValueError("The Phone Number must be set")
        user = self.model(number=number,password = password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, number, password, **kwargs):
        user = self.model(number=number, password = password, **kwargs)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        
        # If did not work set some more boolean fields true LOL

        user.set_password(password)
        user.save()
        return user