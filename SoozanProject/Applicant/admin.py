from django.contrib import admin
from Applicant.models import Applicant

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Applicant, AuthorAdmin)
