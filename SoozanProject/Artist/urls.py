from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.ArtistViewSet)

urlpatterns = [
    path('artist', include(router.urls))
]