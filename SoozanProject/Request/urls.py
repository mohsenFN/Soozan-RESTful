from django.urls import path
from . import views

urlpatterns = [
    path('new', views.NewRequest),
    path('all', views.ListRequests)
]