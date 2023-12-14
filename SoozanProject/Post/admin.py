from django.contrib import admin
from Post.models import Post

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, AuthorAdmin)
