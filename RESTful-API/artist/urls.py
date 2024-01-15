from django.urls import include, path

from artist import views


urlpatterns = [
    path('profile/<int:user_id>', views.artist_profile)
]