#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class NoteBook(models.Model):
    family_name = models.CharField(max_length=40)   # фамилия
    given_name = models.CharField(max_length=40)    # имя
    patronymic = models.CharField(max_length=40)    # отчество
    phon_number = models.CharField(max_length=40)   # телефон
    notes = models.TextField()                      # заметки

