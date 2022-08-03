from core.forms import Form
from .models import Note, NoteItem
from django.forms import inlineformset_factory, BaseInlineFormSet


class NoteForm(Form):
    
    class Meta:
       model = Note
       exclude = ['session', 'term']


class NoteItemInlineFormSet(BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            for k in form.fields:
                form.fields[k].widget.attrs.update({
                    'class': 'form-control'
                })


NoteItemFormSet = inlineformset_factory(
    Note, NoteItem, exclude=[], can_delete=True,
    formset=NoteItemInlineFormSet)
