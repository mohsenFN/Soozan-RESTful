from django.urls import path
from post import views

urlpatterns = [
    path('tags', views.get_tags_list),
    path('new', views.new_post),
    path('update/<int:post_id>', views.update_post)
]