from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Class
from ..forms import ClassForm


@login_required
def index(request):
    classes = Class.objects.all()
    return render(request, 'core/classes_list.html', {
        'title': 'Classes',
        'current_page': 'setting.class.parent',
        'classes': classes,
    })


@login_required
def create(request):
    if request.POST:
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            pass
    else:
        form = ClassForm()
    return render(request, 'object_form.html', {
        'title': 'New class',
        'current_page': 'setting.class.parent',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    if request.POST:
        form = ClassForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            pass
    else:
        form = ClassForm(instance=obj)
    return render(request, 'object_form.html', {
        'title': 'Edit class',
        'current_page': 'setting.class.parent',
        'form': form,
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
        'title': 'Delete class',
        'object': obj,
        'current_page': 'setting.class.parent',
    })
