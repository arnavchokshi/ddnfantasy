from django.db import models
from django.contrib.auth.models import User
from comps.models import Comp
from teams.models import Team

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    DEFAULT_COMPETITIONS = list(Comp.objects.values_list('comp_name', flat=True))
    DEFAULT_TOP_TEAMS = ["","","" ]
    top_teams = models.JSONField(default=dict.fromkeys(DEFAULT_COMPETITIONS, DEFAULT_TOP_TEAMS))
    user_elo = models.IntegerField(default=1000)

    def set_top_teams(self, comp_name, teams):
        self.top_teams[comp_name] = teams
        self.save()

    def get_top_teams(self, comp_name):
        return self.top_teams.get(comp_name)

    def update_elo(self, comp_name, actual_first_place, actual_second_place, actual_third_place):
        predicted_teams = self.get_top_teams(comp_name)
        if not predicted_teams:
            return  # Do not update ELO if predicted teams are empty or None
        predicted_teams_cleaned = [team.strip() for team in predicted_teams]
        actual_teams = [actual_first_place.team_name, actual_second_place.team_name, actual_third_place.team_name]
        if None in actual_teams:
            return  # Do not update ELO if any actual placings are None
        actual_teams_cleaned = [team.strip() for team in actual_teams]
        self.user_elo = 1000

        print(actual_teams_cleaned)
        print(predicted_teams_cleaned)
        
        points = 0
        for i in range(3):
            if predicted_teams_cleaned[i] == actual_teams_cleaned[i]:
                points += 15
            elif predicted_teams_cleaned[i] in actual_teams_cleaned:
                points += 10
            elif i < len(predicted_teams_cleaned) and predicted_teams_cleaned[i] in actual_teams_cleaned:
                points += 5
            else:
                points -= 5

        # Update user's ELO
        self.user_elo += points
        self.save()
