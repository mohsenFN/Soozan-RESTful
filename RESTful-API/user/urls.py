from django.urls import path
from . import views

urlpatterns = [
    path('register', views.user_register, name='user-register'),
    path('get-token', views.user_login, name='get-token'),
    path('refresh-token', views.new_token, name='refresh-token'),
    path('delete', views.delete_user, name='user-delete'),
    path('logout', views.user_logout, name='user-logout')
]
