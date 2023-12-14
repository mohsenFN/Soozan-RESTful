from django.contrib import admin
from Request.models import Request

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Request, AuthorAdmin)
