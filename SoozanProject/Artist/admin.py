from django.contrib import admin
from Artist.models import DerivedArtist

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(DerivedArtist, AuthorAdmin)
