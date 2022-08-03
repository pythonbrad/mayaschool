from core.forms import PersonForm, Form
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ClassTitular


class StaffForm(PersonForm):
    diploma = forms.CharField(max_length=255, label=_("diploma").capitalize())


class ClassTitularForm(Form):

    class Meta:
        model = ClassTitular
        exclude = ['session']
