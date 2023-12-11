# Infi/source/web_project/hello/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]



