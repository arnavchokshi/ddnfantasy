from django.http import HttpResponse
from django.shortcuts import render
from .models import Team

def teams(request):
    teams = Team.objects.all()  # Corrected to execute the queryset
    return render(request, 'teams.html', {'teams': teams})