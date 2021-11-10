from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from web.models import Sex, Analyses, Patients


@login_required
def login(request):
    return render(request, 'registration/login.html')