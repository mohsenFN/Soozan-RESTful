from django.urls import path
from . import views

urlpatterns = [
    path('register', views.user_register),
    path('login', views.user_login),
    path('del', views.delete_user),
    path('refresh-token', views.new_token)
]