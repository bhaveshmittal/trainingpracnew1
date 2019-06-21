# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms
from movieapp.models import movie

def indexview(request):
    return render(request,"movieapp/index.html")

def addview(request):
    form=forms.movieform()
    if request.method=="POST":
        form=forms.movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return indexview(request)
        print("FORM DATA PRINTED SUCCESSFULLY")
    return render(request,'movieapp/add.html',{'form':form})

def listview(request):
    movielist=movie.objects.all()
    return render(request,"movieapp/list.html",{'movielist':movielist})


# Create your views here.
