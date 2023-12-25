from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
''' Vendor '''
from User.models import User

class UserAdminClass(UserAdmin):

    
    search_fields = ["number", "id"]
    ordering = ["id"]

    
    list_filter = []
    filter_horizontal = []
    fieldsets = []


admin.site.register(User, UserAdminClass)
admin.site.unregister(Group)