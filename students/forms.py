from django import forms
from .models import Student
from core.models import SubClass
from core.forms import Form


def get_subclass_choices():
    return ((i.pk, i.name) for i in SubClass.objects.filter())


class StudentForm(Form):
    current_class = forms.ChoiceField(choices=get_subclass_choices)

    class Meta:
        model = Student
        exclude = ['date_of_admission', 'matricule']