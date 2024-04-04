from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm
from .models import UserProfile
from realPlacings.models import Placings
from django.shortcuts import render
from .models import UserProfile
from comps.models import Comp
from realPlacings.models import Placings
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    # Get all the competitions the user has data for
    user_comps = profile.top_teams.keys()

    # Iterate over each competition
    for comp_name in user_comps:
        try:
            # Retrieve the latest placings for the competition
            latest_placings = Placings.objects.filter(comp_name__comp_name=comp_name).latest('id')
            if latest_placings.actual_first_place and latest_placings.actual_second_place and latest_placings.actual_third_place:
                # Update the ELO for the current competition
                profile.update_elo(
                    comp_name,
                    latest_placings.actual_first_place,
                    latest_placings.actual_second_place,
                    latest_placings.actual_third_place
                )
        except Placings.DoesNotExist:
            # Handle the case where Placings object does not exist
            pass

    context = {
        'user': user,
        'profile': profile,
        'comps': Comp.objects.all()
    }

    return render(request, 'profile.html', context)

