from django import forms
from .models import Class, SubClass


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
