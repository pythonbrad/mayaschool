from django.shortcuts import render, redirect, get_object_or_404
from students.models import ClassStudent
from staffs.models import Staff
from .models import AcademicSession, AcademicTerm, SubClass, Class
from finance.models import Invoice
from django.contrib.auth.decorators import login_required
from .forms import ClassForm, SubClassForm, AcademicSessionForm, AcademicTermForm


@login_required
def index(request):
    return render(request, 'core/dashboard.html', {
        'title': 'Dashboard',
        'current_page': 'dashboard',
        'nb_students': ClassStudent.objects.filter(
            session=request.current_session, student__status='active').count(),
        'nb_staffs': Staff.objects.filter(
            status='active').count(),
        'nb_classes': SubClass.objects.count(),
        'total_incomes': sum([
            invoice.total_amount_paid() for invoice in Invoice.objects.filter(
                session=request.current_session
            )
        ]),
    })


@login_required
def classes(request):
    classes = Class.objects.all()
    return render(request, 'core/classes_list.html', {
        'title': 'Classes',
        'current_page': 'setting.class.parent',
        'classes': classes,
    })


@login_required
def new_class(request):
    if request.POST:
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            pass
    else:
        form = ClassForm()
    return render(request, 'new_object.html', {
        'title': 'New class',
        'current_page': 'setting.class.parent',
        'form': form
    })


@login_required
def edit_class(request, pk):
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
    return render(request, 'new_object.html', {
        'title': 'Edit class',
        'current_page': 'setting.class.parent',
        'form': form,
    })


@login_required
def delete_class(request, pk):
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


@login_required
def subclasses(request):
    subclasses = SubClass.objects.all()
    return render(request, 'core/subclasses_list.html', {
        'title': 'Subclasses',
        'current_page': 'setting.class.child',
        'subclasses': subclasses,
    })


@login_required
def new_subclass(request):
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
def edit_subclass(request, pk):
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
def delete_subclass(request, pk):
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


@login_required
def sessions(request):
    sessions = AcademicSession.objects.all()
    return render(request, 'core/sessions_list.html', {
        'title': 'Sessions',
        'current_page': 'setting.session',
        'sessions': sessions,
    })


@login_required
def new_session(request):
    if request.POST:
        form = AcademicSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions')
        else:
            pass
    else:
        form = AcademicSessionForm()
    return render(request, 'new_object.html', {
        'title': 'New session',
        'current_page': 'setting.session',
        'form': form
    })


@login_required
def edit_session(request, pk):
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
    return render(request, 'new_object.html', {
        'title': 'Edit session',
        'current_page': 'setting.session',
        'form': form,
    })


@login_required
def delete_session(request, pk):
    obj = get_object_or_404(AcademicSession, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('sessions')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete session',
        'object': obj,
        'current_page': 'setting.session',
    })


@login_required
def terms(request):
    terms = AcademicTerm.objects.all()
    return render(request, 'core/terms_list.html', {
        'title': 'Terms',
        'current_page': 'setting.term',
        'terms': terms,
    })


@login_required
def new_term(request):
    if request.POST:
        form = AcademicTermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terms')
        else:
            pass
    else:
        form = AcademicTermForm()
    return render(request, 'new_object.html', {
        'title': 'New session',
        'current_page': 'setting.term',
        'form': form
    })


@login_required
def edit_term(request, pk):
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
    return render(request, 'new_object.html', {
        'title': 'Edit term',
        'current_page': 'setting.term',
        'form': form,
    })


@login_required
def delete_term(request, pk):
    obj = get_object_or_404(AcademicTerm, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('terms')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete term',
        'object': obj,
        'current_page': 'setting.term',
    })
