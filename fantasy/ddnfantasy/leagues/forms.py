from django import forms
from .models import League

class LeagueCreationForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'league_id']
