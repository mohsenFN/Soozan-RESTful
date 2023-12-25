from django.urls import path
from . import views

urlpatterns = [
    path('id/<int:user_id>', views.SingleUserView),
    path('register', views.Register),
    path('login', views.Signin)
]