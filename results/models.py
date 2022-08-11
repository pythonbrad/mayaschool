from django.db import models
from django.db.models import Avg
from students.models import ClassStudent
from core.models import AcademicSession, AcademicTerm, Subject
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Note(models.Model):
    class_student = models.ForeignKey(ClassStudent,
        on_delete=models.CASCADE, verbose_name=_("class_student"))
    subject = models.ForeignKey(Subject,
        on_delete=models.CASCADE, verbose_name=_("subject"))
    session = models.ForeignKey(AcademicSession,
        on_delete=models.CASCADE, default=AcademicSession.get_current, verbose_name=_("session"))
    term = models.ForeignKey(AcademicTerm,
        on_delete=models.CASCADE, default=AcademicTerm.get_current, verbose_name=_("term"))

    class Meta:
        ordering = ["subject"]
        unique_together = (('class_student', 'subject', 'session', 'term'),)

    def __str__(self):
        return f"{self.class_student.student} {self.subject} {self.term}"

    def get_value(self):
        value = self.noteitem_set.aggregate(value=Avg('value'))
        return value['value'] or 0.0


class NoteItem(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name=_("note"))
    value = models.DecimalField(default=0.0, decimal_places=2, max_digits=4, verbose_name=_("value"))
    description = models.CharField(max_length=200, verbose_name=_("description"))

    class Meta:
        verbose_name = _("note_item").capitalize()