from django import forms
from .models import AvailableDates

class EventDateUpdateForm(forms.ModelForm):
    class Meta:
        model = AvailableDates
        fields = ['date_from', 'date_to']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }