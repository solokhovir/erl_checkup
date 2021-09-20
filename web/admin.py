from django.contrib import admin

from .models import Analyses, Patients, Reports

admin.site.register(Analyses)
admin.site.register(Patients)
admin.site.register(Reports)
