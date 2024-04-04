from django.urls import path

from . import views

urlpatterns = [
    path("", views.comps, name="comps"),
    path('<int:comp_id>/competing_teams/', views.competing_teams, name='competing_teams'),
]