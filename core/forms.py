from django import forms
from .models import Class, SubClass, AcademicSession, AcademicTerm, Subject, Person, SystemConfig, Module
from django.forms import inlineformset_factory, BaseInlineFormSet

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


class SubClassInlineFormSet(BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            for k in form.fields:
                form.fields[k].widget.attrs.update({
                    'class': 'form-control'
                })

SubClassFormSet = inlineformset_factory(
    Class, SubClass, exclude=[], can_delete=True,
    formset=SubClassInlineFormSet)


class AcademicSessionForm(Form):

    class Meta:
        model = AcademicSession
        exclude = []


class AcademicTermForm(Form):

    class Meta:
        model = AcademicTerm
        exclude = []


class ModuleForm(Form):

    class Meta:
        model = Module
        exclude = []


class SubjectInlineFormSet(BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            for k in form.fields:
                form.fields[k].widget.attrs.update({
                    'class': 'form-control'
                })

SubjectFormSet = inlineformset_factory(
    Module, Subject, exclude=[], can_delete=True,
    formset=SubjectInlineFormSet)


class PersonForm(Form):

    class Meta:
        model = Person
        exclude = ['joined_date', 'matricule']


class SystemConfigForm(Form):

    class Meta:
        model = SystemConfig
        exclude = []
