from core.forms import PersonForm
from django import forms
from django.utils.translation import gettext as _


class StaffForm(PersonForm):
    diploma = forms.CharField(max_length=255, label=_("diploma").capitalize())
