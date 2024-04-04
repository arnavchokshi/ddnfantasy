from django.db import models
from teams.models import Team

class Comp(models.Model):
    comp_name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.comp_name
