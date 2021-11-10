# -*- coding: utf8 -*-
from django.db import models


class Sex(models.Model):
    sex_main = models.CharField('Пол', max_length=20)

    class Meta:
        verbose_name_plural = 'Пол'
        verbose_name = 'Пол'

    def __str__(self):
        return self.sex_main


# Создание базы данных с пациентами
class Patients(models.Model):
    name = models.CharField('ФИО', max_length=1000)
    birthday = models.DateField('Дата рождения', null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name=u"Пол")
    is_confirm_consent = models.BooleanField('Согласие на обработку данных', default=False)
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
    taken_date = models.DateField('Дата исследования', null=True)
    # group_number = models.IntegerField()
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name=u"ФИО Пациента")

    leukocyte = models.FloatField('Лейкоциты - WBC')
    lymphocytes = models.FloatField('Лимфоциты - LYM%')
    monocytes = models.FloatField('Моноциты - MON%')
    basophils = models.FloatField('Базофилы - BAS%')
    eosinophils = models.FloatField('Эозинофилы - EOS%')
    neutrophils = models.FloatField('Нейтрофилы - NEUT%')
    young = models.FloatField('Юные - IMM%')
    myelocytes = models.FloatField('Миелоциты')
    toxic_grit = models.FloatField('Токсическая зернистость')
    plasma = models.FloatField('Плазматические клетки')

    # stab = models.IntegerField()
    # segmented = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Анализы'
        verbose_name = 'Анализ'

    def __str__(self):
        return self.taken_date


# class Reports(models.Model):
#     report = models.ForeignKey(Analyses, on_delete=models.CASCADE)
