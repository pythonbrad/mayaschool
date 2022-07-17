from django import forms
from .models import Student
from core.models import SubClass


class StudentForm(forms.ModelForm):
    current_class = forms.ChoiceField(choices=[(i.pk, i.name) for i in SubClass.objects.all()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in self.fields:
            self.fields[k].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Student
        exclude = ['date_of_admission']
