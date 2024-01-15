from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('artist/', include('artist.urls')),
    path('post/', include('post.urls'))
]