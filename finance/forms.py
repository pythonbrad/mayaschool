from core.forms import Form
from .models import Invoice, InvoiceItem, Receipt
from django.forms import inlineformset_factory, BaseInlineFormSet


class InvoiceForm(Form):
    
    class Meta:
       model = Invoice
       exclude = ['session']


class InvoiceItemInlineFormSet(BaseInlineFormSet):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            for k in form.fields:
                form.fields[k].widget.attrs.update({
                    'class': 'form-control'
                })


class ReceiptForm(Form):

    class Meta:
       model = Receipt
       exclude = ['date_paid']


InvoiceItemFormSet = inlineformset_factory(
    Invoice, InvoiceItem, exclude=[], can_delete=True,
    formset=InvoiceItemInlineFormSet)
