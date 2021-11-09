from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sex, Patients, Analyses


class AnalysesView(APIView):
    def get(self, request):
        analyses = Analyses.objects.all()
        return Response({"analyses": analyses})


class SexView(APIView):
    def get(self, request):
        sex = Sex.objects.all()
        return Response({'sex': sex})


class PatientsView(APIView):
    def get(self, request):
        patients = Patients.objects.all()
        return Response({'patients': patients})
