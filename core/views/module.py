from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from ..models import Module
from ..forms import ModuleForm, SubjectFormSet


@login_required
def index(request):
    modules = Module.objects.all()
    return render(request, 'core/modules_list.html', {
        'title': _('modules_list').capitalize(),
        'current_page': 'setting.module',
        'modules': modules,
    })


@login_required
def create(request):
    if request.POST:
        module_form = ModuleForm(request.POST)
        subjects_form = SubjectFormSet(request.POST)
        if module_form.is_valid() and subjects_form.is_valid():
            module_form.save()
            subjects_form.instance = module_form.instance
            subjects_form.save()
            return redirect('modules')
        else:
            pass
    else:
        module_form = ModuleForm()
        subjects_form = SubjectFormSet()
    return render(request, 'core/module_form.html', {
        'title': _('add_module').capitalize(),
        'current_page': 'setting.module',
        'form': module_form,
        'items': subjects_form,
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Module, pk=pk)
    if request.POST:
        module_form = ModuleForm(request.POST, instance=obj)
        subjects_form = SubjectFormSet(request.POST, instance=obj)
        if module_form.is_valid() and subjects_form.is_valid():
            module_form.save()
            subjects_form.save()
            return redirect('modules')
        else:
            pass
    else:
        module_form = ModuleForm(instance=obj)
        subjects_form = SubjectFormSet(instance=obj)
    return render(request, 'core/module_form.html', {
        'title': _('edit_module').capitalize(),
        'current_page': 'setting.module',
        'form': module_form,
        'items': subjects_form
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Module, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('modules')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_module').capitalize(),
        'object': obj,
        'current_page': 'setting.module',
    })
