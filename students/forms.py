from django import forms
from core.models import SubClass
from core.forms import PersonForm


def get_subclass_choices():
    return ((i.pk, i.name) for i in SubClass.objects.all())


class StudentForm(PersonForm):
    current_class = forms.ChoiceField(choices=get_subclass_choices)
    guardian_name = forms.CharField(max_length=255)
