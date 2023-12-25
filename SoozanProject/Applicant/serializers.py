from rest_framework import serializers
from Applicant.models import Applicant


class ApplicantDashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['user', 'full_name', 'location']