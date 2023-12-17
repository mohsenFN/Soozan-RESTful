from django.urls import include, path
from rest_framework import routers
from Applicant.views import ApplicantViewSet

router = routers.DefaultRouter()
router.register('', ApplicantViewSet)

urlpatterns = [
    path('applicant', include(router.urls))
]