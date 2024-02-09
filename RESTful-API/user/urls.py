from django.urls import path
from . import views

urlpatterns = [
    path('register', views.user_register),
    path('get-token', views.user_login),
    path('refresh-token', views.new_token),
    path('delete', views.delete_user),
    path('logout', views.user_logout)
]
