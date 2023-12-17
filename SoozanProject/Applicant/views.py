from rest_framework import viewsets
from Applicant.serializers import ApplicantSerializer
from Applicant.models import Applicant

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer