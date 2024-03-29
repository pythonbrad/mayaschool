from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from ..models import AcademicSession
from ..forms import AcademicSessionForm


@login_required
def index(request):
    sessions = AcademicSession.objects.all()
    return render(request, 'core/sessions_list.html', {
        'title': _('sessions_list').capitalize(),
        'current_page': 'setting.session',
        'sessions': sessions,
    })


@login_required
def create(request):
    if request.POST:
        form = AcademicSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions')
        else:
            pass
    else:
        form = AcademicSessionForm()
    return render(request, 'object_form.html', {
        'title': _('add_session').capitalize(),
        'current_page': 'setting.session',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(AcademicSession, pk=pk)
    if request.POST:
        form = AcademicSessionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('sessions')
        else:
            pass
    else:
        form = AcademicSessionForm(instance=obj)
    return render(request, 'object_form.html', {
        'title': _('edit_session').capitalize(),
        'current_page': 'setting.session',
        'form': form,
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(AcademicSession, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('sessions')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_session').capitalize(),
        'object': obj,
        'current_page': 'setting.session',
    })
