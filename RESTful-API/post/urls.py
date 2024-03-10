from django.urls import path
from post import views

urlpatterns = [
    path('tags', views.get_tags_list, name='get-tags'),
    path('new', views.new_post, name='post-new'),
    path('update/<int:post_id>', views.update_post, name='post-update'),
    path('delete/<int:post_id>', views.delete_post, name='post-delete')
]