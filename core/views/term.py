from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from ..models import AcademicTerm
from ..forms import AcademicTermForm


@login_required
def index(request):
    terms = AcademicTerm.objects.all()
    return render(request, 'core/terms_list.html', {
        'title': _('terms_list').capitalize(),
        'current_page': 'setting.term',
        'terms': terms,
    })


@login_required
def create(request):
    if request.POST:
        form = AcademicTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terms')
        else:
            pass
    else:
        form = AcademicTermForm()
    return render(request, 'object_form.html', {
        'title': _('add_session').capitalize(),
        'current_page': 'setting.term',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(AcademicTerm, pk=pk)
    if request.POST:
        form = AcademicTermForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('terms')
        else:
            pass
    else:
        form = AcademicTermForm(instance=obj)
    return render(request, 'object_form.html', {
        'title': _('edit_term').capitalize(),
        'current_page': 'setting.term',
        'form': form,
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(AcademicTerm, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('terms')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_term').capitalize(),
        'object': obj,
        'current_page': 'setting.term',
    })
