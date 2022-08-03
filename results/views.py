from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .models import Note
from .forms import NoteForm, NoteItemFormSet


@login_required
def index(request):
    notes = request.current_session.note_set.all()
    return render(request, 'results/notes_list.html', {
        'title': _('notes_list').capitalize(),
        'current_page': 'result.note',
        'notes': notes,
    })


@login_required
def create(request):
    if request.POST:
        note_form = NoteForm(request.POST)
        note_items_form = NoteItemFormSet(request.POST)
        if note_form.is_valid() and note_items_form.is_valid():
            note_form.save()
            note_items_form.instance = note_form.instance
            note_items_form.save()
            return redirect('notes')
        else:
            pass
    else:
        note_form = NoteForm()
        note_items_form = NoteItemFormSet()
    return render(request, 'results/note_form.html', {
        'title': _('add_note').capitalize(),
        'current_page': 'result.note',
        'form': note_form,
        'items': note_items_form,
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Note, pk=pk)
    if request.POST:
        note_form = NoteForm(request.POST, instance=obj)
        note_items_form = NoteItemFormSet(request.POST, instance=obj)
        if note_form.is_valid() and note_items_form.is_valid():
            note_form.save()
            note_items_form.save()
            return redirect('notes')
        else:
            print(note_form.errors, note_items_form.errors)
    else:
        note_form = NoteForm(instance=obj)
        note_items_form = NoteItemFormSet(instance=obj)
    return render(request, 'results/note_form.html', {
        'title': _('edit_note').capitalize(),
        'current_page': 'result.note',
        'form': note_form,
        'items': note_items_form
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Note, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('notes')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': _('delete_note').capitalize(),
        'object': obj,
        'current_page': 'result.note',
    })


@login_required
def generate_report_cards(request):
    notes = request.current_session.note_set.all()
    return render(request, 'results/notes_list.html', {
        'title': _('notes_list').capitalize(),
        'current_page': 'result.report_card',
        'notes': notes,
    })