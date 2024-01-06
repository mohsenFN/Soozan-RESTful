from django.urls import path
from . import views

urlpatterns = [
    path('register', views.user_register),
    path('login', views.user_login),
    path('dash', views.get_user_dashboard),
    path('del', views.delete_user)
]