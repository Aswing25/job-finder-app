from django.shortcuts import render
from jobapp.models import jobdb
# Create your views here.

def indexpage(req):
    return render(req,"index.html")

def aboutpage(req):
    return render(req,"about.html")