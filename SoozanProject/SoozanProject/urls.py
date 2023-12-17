from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('User.urls')),
    path('api/', include('Artist.urls')),
    path('api/', include('Applicant.urls'))
]