from django.urls import path
from Post import views

urlpatterns = [
    path('tags', views.get_tags_list),
]