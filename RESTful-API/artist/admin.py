from django.contrib import admin
from artist.models import Artist

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, AuthorAdmin)