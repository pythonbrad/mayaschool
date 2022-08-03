from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .models import Invoice, Receipt
from .forms import InvoiceForm, ReceiptForm, InvoiceItemFormSet


@login_required
def invoices(request):
    return render(request, 'finance/invoices_list.html', {
        'title': _('invoices_list').capitalize(),
        'current_page': 'invoice',
        'invoices': request.current_session.invoice_set.all()
    })


@login_required
def invoice_details(request, pk):
    obj = get_object_or_404(Invoice, pk=pk)
    return render(request, 'finance/invoice_details.html', {
        'invoice': obj,
        'items': obj.invoiceitem_set.all(),
        'receipts': obj.receipt_set.all(),
        'title': _('invoice_details').capitalize(),
        'current_page': 'invoice',
    })


@login_required
def create_invoice(request):
    if request.POST:
        invoice_form = InvoiceForm(request.POST)
        invoice_items_form = InvoiceItemFormSet(request.POST)
        if invoice_form.is_valid() and invoice_items_form.is_valid():
            invoice_form.save()
            invoice_items_form.instance = invoice_form.instance
            invoice_items_form.save()
            return redirect('invoices')
        else:
            pass
    else:
        invoice_form = InvoiceForm()
        invoice_items_form = InvoiceItemFormSet()
    return render(request, 'finance/invoice_form.html', {
        'title': _('add_invoice').capitalize(),
        'current_page': 'invoice',
        'form': invoice_form,
        'items': invoice_items_form,
    })


@login_required
def edit_invoice(request, pk):
    obj = get_object_or_404(Invoice, pk=pk)
    if request.POST:
        invoice_form = InvoiceForm(request.POST, instance=obj)
        invoice_items_form = InvoiceItemFormSet(request.POST, instance=obj)
        if invoice_form.is_valid() and invoice_items_form.is_valid():
            invoice_form.save()
            invoice_items_form.save()
            return redirect('invoices')
        else:
            pass
    else:
        invoice_form = InvoiceForm(instance=obj)
        invoice_items_form = InvoiceItemFormSet(instance=obj)
    return render(request, 'finance/invoice_form.html', {
        'title': _('edit_invoice').capitalize(),
        'current_page': 'invoice',
        'form': invoice_form,
        'items': invoice_items_form
    })


@login_required
def delete_invoice(request, pk):
    obj = get_object_or_404(Invoice, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('invoices')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_invoice').capitalize(),
        'object': obj,
        'current_page': 'invoice',
    })


@login_required
def create_receipt(request, pk):
    obj = get_object_or_404(Invoice, pk=pk)
    if request.POST:
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.instance.invoice = obj
            form.save()
            return redirect('invoice_details', pk=pk)
        else:
            pass
    else:
        form = ReceiptForm()
    return render(request, 'finance/receipt_form.html', {
        'title': _('add_receipt').capitalize(),
        'invoice': obj,
        'current_page': 'invoice',
        'form': form
    })


@login_required
def edit_receipt(request, id, pk):
    obj = get_object_or_404(Receipt, pk=pk, invoice_id=id)
    if request.POST:
        form = ReceiptForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('invoice_details', pk=id)
        else:
            pass
    else:
        form = ReceiptForm(instance=obj)
    return render(request, 'finance/receipt_form.html', {
        'title': _('edit_receipt').capitalize(),
        'invoice': get_object_or_404(Invoice, pk=id),
        'current_page': 'invoice',
        'form': form
    })


@login_required
def delete_receipt(request, id, pk):
    obj = get_object_or_404(Receipt, pk=pk, invoice_id=id)
    if request.POST:
        obj.delete()
        return redirect('invoice_details', pk=id)
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_receipt').capitalize(),
        'object': obj,
        'current_page': 'receipt',
    })
