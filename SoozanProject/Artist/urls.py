from django.urls import include, path

from Artist import views



urlpatterns = [
    path('update', views.UpdateArtist),
]