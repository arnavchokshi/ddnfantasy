from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.team_name