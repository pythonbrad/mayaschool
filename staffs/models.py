from django.db import models
from django.utils.translation import gettext as _
from core.models import AcademicSession, Subject, SubClass, Person


class Staff(models.Model):
    """Staff."""

    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name=_('person'))
    diploma = models.CharField(blank=True, max_length=255, verbose_name=_('diploma'))
    tag = 'P'

    class Meta:
        verbose_name = _('staff').capitalize()

    def is_teacher(self):
        return self.classteacher_set.exists()

    def save(self, *args, **kwargs):
        """Save."""
        super().save(*args, **kwargs)
        if not self.person.matricule:
            self.person.generate_matricule(self)
        else:
            pass


class ClassTeacher(models.Model):
    """Teacher of a class."""

    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('teacher'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject'))
    subclass = models.ForeignKey(SubClass, on_delete=models.CASCADE, verbose_name=_('subclass'))
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current, verbose_name=_('session'))

    class Meta:
        unique_together = (('teacher', 'session', 'subject', 'subclass'),)
        verbose_name = _('class_teacher').capitalize()
