# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class movie(models.Model):

    name=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    year=models.IntegerField()
    earning=models.IntegerField()
