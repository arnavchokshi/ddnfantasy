from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from comps.models import Comp

def comps(request):
    comps = Comp.objects.all()  # Corrected to execute the queryset
    return render(request, 'comps.html', {'comps': comps})

def competing_teams(request, comp_id):
    # Retrieve the competition object or return a 404 error if not found
    competition = get_object_or_404(Comp, pk=comp_id)
    # Retrieve teams attending the competition
    teams = competition.teams.all()
    return render(request, 'competing_teams.html', {'competition': competition, 'teams': teams})