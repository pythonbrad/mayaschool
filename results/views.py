from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .models import Note
from .forms import NoteForm, NoteItemFormSet
from students.models import Student
from core.models import Class


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
    notes = []

    if request.GET:
        subclass_id = request.GET.get('subclass', '')

        if subclass_id.isdigit():
            notes = request.current_session.note_set.filter(
                term=request.current_term,
                class_student__subclass_id=subclass_id
            )
        else:
            pass

    options = {
        i.pk: {
            'name': i.name,
            'classes': {
                ii.pk: ii.name for ii in i.subclass_set.all()
            },
        } for i in Class.objects.all()
    }

    stats = {
        'min': None,
        'max': None,
        'avg': 0,
    }
    data = {}

    for note in notes:
        class_student = note.class_student
        subject = note.subject
        value = note.get_value()

        # We set the dict
        if subject not in stats:
            stats[subject] = {
                'min': None,
                'max': None,
                'avg': 0,
            }
        if class_student not in data:
            data[class_student] = {
                'subject': {},
                'value': 0,
                'rank': None
            }

        # We update the dict
        # Stats
        if stats[subject]['min'] == None or value < stats[subject]['min']:
            stats[subject]['min'] = value
        if stats[subject]['max'] == None or value > stats[subject]['max']:
            stats[subject]['max'] = value

        stats[subject]['avg'] += value

        # Data
        data[class_student]['subject'][subject] = {
            'value': value,
            'rank': None,
            'class_stats': stats[subject],
        }
        data[class_student]['value'] += value

    # We update the stats
    for class_student in data:
        data[class_student]['value'] /= len(data[class_student]['subject'])
        data[class_student]['avg'] = data[class_student]['value'] / 20 * 100
        stats['avg'] += data[class_student]['value']

        if stats['min'] == None or data[class_student]['value'] < stats['min']:
            stats['min'] = data[class_student]['value']
        if stats['max'] == None or data[class_student]['value'] > stats['max']:
            stats['max'] = data[class_student]['value']
    
    stats['avg'] /= len(data) or 1

    for subject in stats:
        if isinstance(stats[subject], dict):
            # avg by subject
            stats[subject]['avg'] /= len(data) or 1

            # rank by subject
            _list = sorted(
                data.keys(),
                reverse=True,
                key=lambda class_student:data[class_student]['subject'][subject]['value']
            )
            for class_student in data:
                data[class_student]['subject'][subject]['rank'] = _list.index(class_student) + 1

    # rank
    _list = sorted(
        data.keys(),
        reverse=True,
        key=lambda x:data[x]['value']
    )
    for class_student in data:
        data[class_student]['rank'] = _list.index(class_student) + 1


    return render(request, 'results/report_cards_list.html', {
        'title': _('report_cards_list').capitalize(),
        'current_page': 'result.report_card',
        'data': data,
        'options': options,
        'stats': stats
    })
