from django import forms
from .models import Student
from core.models import SubClass
from core.forms import Form

class StudentForm(Form):
    current_class = forms.ChoiceField(choices=[(i.pk, i.name) for i in SubClass.objects.all()])

    class Meta:
        model = Student
        exclude = ['date_of_admission', 'matricule']
