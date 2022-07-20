from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import SubClass
from ..forms import SubClassForm


@login_required
def index(request):
    subclasses = SubClass.objects.all()
    return render(request, 'core/subclasses_list.html', {
        'title': 'Subclasses',
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
    return render(request, 'new_object.html', {
        'title': 'New subclass',
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
    return render(request, 'new_object.html', {
        'title': 'Edit subclass',
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
        'title': 'Delete subject',
        'object': obj,
        'current_page': 'setting.class.child',
    })
