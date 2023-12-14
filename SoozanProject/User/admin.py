from django.contrib import admin
from User.models import User

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, AuthorAdmin)
