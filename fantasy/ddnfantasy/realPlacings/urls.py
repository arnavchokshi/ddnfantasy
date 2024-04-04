from django.urls import path
from . import views

urlpatterns = [
    path("", views.real_placings, name="real_placings"),
]