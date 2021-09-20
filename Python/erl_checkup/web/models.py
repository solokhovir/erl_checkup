# -*- coding: utf8 -*-
from django.db import models


class Sex(models.Model):
    sex_main = models.CharField('Пол', max_length=20)


# Создание базы данных с пациентами
class Patients(models.Model):
    name = models.CharField('ФИО', max_length=1000)
    birthday = models.DateField('Дата рождения')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    is_confirm_consent = models.BooleanField('Согласие на обработку данных')
    email = models.EmailField('e-mail')
    phone = models.CharField('Телефон', max_length=12)

    class Meta:
        verbose_name_plural = 'ФИО'
        verbose_name = 'ФИО'
        ordering = ['name']

    def __str__(self):
        return self.name


# Создание базы данных с анализами
class Analyses(models.Model):
    taken_date = models.DateField
    group_number = models.IntegerField
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)

    leukocyte = models.CharField
    lymphocytes = models.FloatField
    monocytes = models.FloatField
    basophils = models.FloatField
    eosinophils = models.FloatField
    neutrophils = models.CharField
    young = models.CharField
    myelocytes = models.CharField
    toxic_grit = models.CharField
    plasma = models.CharField

    stab = models.CharField
    segmented = models.CharField


class Reports(models.Model):
    report = models.ForeignKey(Analyses, on_delete=models.CASCADE)
