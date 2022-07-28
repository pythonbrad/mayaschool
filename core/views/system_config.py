from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import SystemConfig
from ..forms import SystemConfigForm


@login_required
def index(request):
    system_configs = SystemConfig.objects.all()
    return render(request, 'core/system_configs_list.html', {
        'title': 'System Configs',
        'current_page': 'setting.system_config',
        'system_configs': system_configs,
    })


@login_required
def create(request):
    if request.POST:
        form = SystemConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_configs')
        else:
            pass
    else:
        form = SystemConfigForm()
    return render(request, 'object_form.html', {
        'title': 'New system_config',
        'current_page': 'setting.system_config',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(SystemConfig, pk=pk)
    if request.POST:
        form = SystemConfigForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('system_configs')
        else:
            pass
    else:
        form = SystemConfigForm(instance=obj)
    return render(request, 'object_form.html', {
        'title': 'Edit system_config',
        'current_page': 'setting.system_config',
        'form': form,
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(SystemConfig, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('system_configs')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete system_config',
        'object': obj,
        'current_page': 'setting.system_config',
    })
