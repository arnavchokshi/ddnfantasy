from django.db import models
from comps.views import Comp
from teams.views import Team

class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice, related_name='choices')
    has_voted = models.BooleanField(default=False)  # New boolean field

    def __str__(self):
        return self.question_text