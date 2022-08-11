from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AcademicSession, SubClass, Person


class Student(models.Model):
    """Student."""

    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name=_("person"))
    guardian = models.CharField(max_length=255, verbose_name=_("guardian"))
    tag = 'S'

    class Meta:
        verbose_name = _("student").capitalize()

    def __str__(self):
        return f"{self.person} ({self.person.matricule})"

    def save(self, *args, **kwargs):
        """Save."""
        super().save(*args, **kwargs)
        if not self.person.matricule:
            self.person.generate_matricule(self)
        else:
            pass

    def get_current_class(self):
        return self.classstudent_set.get(session=AcademicSession.get_current())


class ClassStudent(models.Model):
    """Student of a class."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("student"))
    subclass = models.ForeignKey(SubClass, on_delete=models.CASCADE, verbose_name=_("subclass"))
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current, verbose_name=_("session"))

    class Meta:
        unique_together = (('student', 'session'),)
