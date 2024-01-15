from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('artist/', include('Artist.urls')),
    path('post/', include('Post.urls'))
]