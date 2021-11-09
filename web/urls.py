from django.urls import path
from .apiviews import AnalysesView

app_name = "erl_checkup"

urlpatterns = [
    path('analyses/', AnalysesView.as_view()),
]