from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('user', include(router.urls)),
    path('user/<int:user_id>', views.SingleUserView)
]