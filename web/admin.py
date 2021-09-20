from django.contrib import admin

from .models import Analyses, Patients, Sex

admin.site.register(Analyses)
admin.site.register(Patients)
admin.site.register(Sex)
