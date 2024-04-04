from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=100)
    league_id = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_leagues')
    members = models.ManyToManyField(User, related_name='joined_leagues')

    def __str__(self):
        return self.name
