from django.db import models
from django.contrib.auth.models import User
from comps.models import Comp
from teams.models import Team

class Placings(models.Model):
    comp_name = models.OneToOneField(Comp, null=True, on_delete=models.CASCADE)
    actual_first_place = models.ForeignKey(Team, related_name='first_place', null=True, on_delete=models.CASCADE)
    actual_second_place = models.ForeignKey(Team, related_name='second_place', null=True, on_delete=models.CASCADE)
    actual_third_place = models.ForeignKey(Team, related_name='third_place', null=True, on_delete=models.CASCADE)
    # Other fields

    def __str__(self):
        return str(self.comp_name)  # Ensure the comp_name is converted to a string

