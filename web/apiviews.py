from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, permissions

from .models import Sex, Patients, Analyses
from .serializers import AnalysesSerializer, PatientsSerializer, SexSerializer


class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SexSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientsSerializer


class AnalysesViewSet(viewsets.ModelViewSet):
    queryset = Analyses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnalysesSerializer


# class AnalysesView(APIView):
#     def get(self, request):
#         analyses = Analyses.objects.all()
#         analyses_serializer = AnalysesSerializer(analyses, many=True)
#         return Response({"analyses": analyses_serializer.data})
#
#
# class SexView(APIView):
#     def get(self, request):
#         sex = Sex.objects.all()
#         sex_serializer = SexSerializer(sex, many=True)
#         return Response({'sex': sex_serializer.data})
#
#
# class PatientsView(APIView):
#     def get(self, request):
#         patients = Patients.objects.all()
#         patients_serializer = PatientsSerializer(patients, many=True)
#         return Response({'patients': patients_serializer.data})
