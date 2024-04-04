from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import League
from .forms import LeagueCreationForm

def leagues(request):
    return render(request, 'leagues.html')


@login_required
def create_league(request):
    if request.method == 'POST':
        form = LeagueCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            league_id = form.cleaned_data['league_id']
            league = League.objects.create(name=name, league_id=league_id, creator=request.user)
            messages.success(request, 'League created successfully!')
            return redirect('my_leagues')
    else:
        form = LeagueCreationForm()
    return render(request, 'create_league.html', {'form': form})

@login_required
def join_league(request):
    if request.method == 'POST':
        league_id = request.POST.get('league_id')
        try:
            league = League.objects.get(league_id=league_id)
            if request.user in league.members.all():
                messages.warning(request, 'You are already a member of this league.')
                return redirect('my_leagues')
            else:
                league.members.add(request.user)
                messages.success(request, 'You have successfully joined the league.')
                # Redirect to the league details page after joining
                return redirect('my_leagues')
        except League.DoesNotExist:
            messages.error(request, 'Invalid league ID. Please enter a valid ID.')
    return render(request, 'join_league.html')

@login_required
def league_details(request, league_id):
    try:
        league = League.objects.get(id=league_id)
        return render(request, 'my_leagues.html', {'league': league})
    except League.DoesNotExist:
        messages.error(request, 'The requested league does not exist.')
        return redirect('leagues')

@login_required
def my_leagues(request):
    user = request.user
    user_leagues = League.objects.filter(members=user)
    return render(request, 'my_leagues.html', {'user_leagues': user_leagues})