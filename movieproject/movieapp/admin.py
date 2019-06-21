# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from movieapp.models import movie
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display=['name','hero','year','earning']


admin.site.register(movie,movieAdmin)
