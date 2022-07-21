from django import forms
from .models import Class, SubClass, AcademicSession, AcademicTerm, Subject, Person


class Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in self.fields:
            self.fields[k].widget.attrs.update({
                'class': 'form-control'
            })

class ClassForm(Form):

    class Meta:
        model = Class
        exclude = []


class SubClassForm(Form):

    class Meta:
        model = SubClass
        exclude = []


class AcademicSessionForm(Form):

    class Meta:
        model = AcademicSession
        exclude = []


class AcademicTermForm(Form):

    class Meta:
        model = AcademicTerm
        exclude = []


class SubjectForm(Form):

    class Meta:
        model = Subject
        exclude = []


class PersonForm(Form):

    class Meta:
        model = Person
        exclude = ['joined_date', 'matricule']
