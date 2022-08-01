from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from ..models import SubClass
from ..forms import SubClassForm


@login_required
def index(request):
    subclasses = SubClass.objects.all()
    return render(request, 'core/subclasses_list.html', {
        'title': _('subclasses_list').capitalize(),
        'current_page': 'setting.class.child',
        'subclasses': subclasses,
    })


@login_required
def create(request):
    if request.POST:
        form = SubClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subclasses')
        else:
            pass
    else:
        form = SubClassForm()
    return render(request, 'object_form.html', {
        'title': _('add_subclass').capitalize(),
        'current_page': 'setting.class.child',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(SubClass, pk=pk)
    if request.POST:
        form = SubClassForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('subclasses')
        else:
            pass
    else:
        form = SubClassForm(instance=obj)
    return render(request, 'object_form.html', {
        'title': _('edit_subclass').capitalize(),
        'current_page': 'setting.class.child',
        'form': form,
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(SubClass, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('subclasses')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_subclass').capitalize(),
        'object': obj,
        'current_page': 'setting.class.child',
    })
