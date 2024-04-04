from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count

def home_page(request):
    return render(request, 'home_page.html')

def update_top_teams(request):
    if request.method == 'POST':
        top_team_name = request.POST.get('top_team_name')  # Get the name of the top team
        second_team_name = request.POST.get('second_team_name')
        third_team_name = request.POST.get('third_team_name')
        competition_name = request.POST.get('competition_name')  # Get the name of the competition
        user_profile = request.user.userprofile

        # Update the top team for the specified competition
        top_teams = user_profile.top_teams
        if competition_name in top_teams:
            top_teams[competition_name][0] = top_team_name  # Update the first team for the competition
            top_teams[competition_name][1] = second_team_name
            top_teams[competition_name][2] = third_team_name
            user_profile.save()  # Save the changes to the user profile
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Competition not found'})

    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
