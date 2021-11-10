from django.urls import path
from rest_framework import routers
from .apiviews import AnalysesViewSet, PatientsViewSet, SexViewSet
from web import views

app_name = "erl_checkup"

router = routers.DefaultRouter()
router.register('analyses', AnalysesViewSet, 'analyses')
router.register('patients', PatientsViewSet, 'patients')
router.register('sex', SexViewSet, 'sex')
path('login', views.login)

urlpatterns = router.urls