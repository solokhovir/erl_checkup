from rest_framework import serializers
from .models import Analyses, Patients, Sex


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'


class AnalysesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyses
        fields = '__all__'
