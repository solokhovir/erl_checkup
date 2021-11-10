from django.contrib import admin

from .models import Analyses, Patients, Sex


class SexAdmin(admin.ModelAdmin):
    list_display = ('sex_main', )
    list_display_links = ('sex_main', )


class PatientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')
    list_display_links = ('name', )
    search_fields = ('name', 'email', 'phone')


class AnalysesAdmin(admin.ModelAdmin):
    list_display = ('taken_date', 'patient')
    list_display_links = ('taken_date', 'patient')
    search_fields = ('taken_date', 'patient')


admin.site.register(Analyses, AnalysesAdmin)
admin.site.register(Patients, PatientsAdmin)
admin.site.register(Sex, SexAdmin)
