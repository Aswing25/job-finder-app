from django.contrib import admin
from django.urls import path
from jobapp import views

urlpatterns= [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage")
]
