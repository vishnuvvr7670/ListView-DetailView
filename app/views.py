from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #ordering=['sname']
    #queryset=School.objects.filter(id__in=(1,3))

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobjects'
