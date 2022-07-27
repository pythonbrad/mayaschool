from core.forms import PersonForm
from django import forms


class StaffForm(PersonForm):
    diploma = forms.CharField(max_length=255)
