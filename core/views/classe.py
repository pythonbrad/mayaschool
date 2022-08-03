from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from ..models import Class
from ..forms import ClassForm, SubClassFormSet


@login_required
def index(request):
    classes = Class.objects.all()
    return render(request, 'core/classes_list.html', {
        'title': _('classes_list').capitalize(),
        'current_page': 'setting.class',
        'classes': classes,
    })


@login_required
def create(request):
    if request.POST:
        class_form = ClassForm(request.POST)
        subclasses_form = SubClassFormSet(request.POST)
        if class_form.is_valid() and subclasses_form.is_valid():
            class_form.save()
            subclasses_form.instance = class_form.instance
            subclasses_form.save()
            return redirect('classes')
        else:
            pass
    else:
        class_form = ClassForm()
        subclasses_form = SubClassFormSet()
    return render(request, 'core/class_form.html', {
        'title': _('add_class').capitalize(),
        'current_page': 'setting.class',
        'form': class_form,
        'items': subclasses_form,
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    if request.POST:
        class_form = ClassForm(request.POST, instance=obj)
        subclasses_form = SubClassFormSet(request.POST, instance=obj)
        if class_form.is_valid() and subclasses_form.is_valid():
            class_form.save()
            subclasses_form.save()
            return redirect('classes')
        else:
            pass
    else:
        class_form = ClassForm(instance=obj)
        subclasses_form = SubClassFormSet(instance=obj)
    return render(request, 'core/class_form.html', {
        'title': _('edit_class').capitalize(),
        'current_page': 'setting.class',
        'form': class_form,
        'items': subclasses_form
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('classes')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_class').capitalize(),
        'object': obj,
        'current_page': 'setting.class',
    })
