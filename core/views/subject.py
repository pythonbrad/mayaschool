from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Subject
from ..forms import SubjectForm


@login_required
def index(request):
    subjects = Subject.objects.all()
    return render(request, 'core/subjects_list.html', {
        'title': 'Subjects',
        'current_page': 'setting.subject',
        'subjects': subjects,
    })


@login_required
def create(request):
    if request.POST:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            pass
    else:
        form = SubjectForm()
    return render(request, 'new_object.html', {
        'title': 'New subject',
        'current_page': 'setting.subject',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Subject, pk=pk)
    if request.POST:
        form = SubjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            pass
    else:
        form = SubjectForm(instance=obj)
    return render(request, 'new_object.html', {
        'title': 'Edit subject',
        'current_page': 'setting.subject',
        'form': form,
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Subject, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('subjects')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete subject',
        'object': obj,
        'current_page': 'setting.subject',
    })
