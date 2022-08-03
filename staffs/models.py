from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AcademicSession, SubClass, Person


class Staff(models.Model):
    """Staff."""

    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name=_('person'))
    diploma = models.CharField(blank=True, max_length=255, verbose_name=_('diploma'))
    tag = 'P'

    class Meta:
        verbose_name = _('staff').capitalize()

    def is_titular(self):
        return self.classtitular_set.exists()

    def save(self, *args, **kwargs):
        """Save."""
        super().save(*args, **kwargs)
        if not self.person.matricule:
            self.person.generate_matricule(self)
        else:
            pass


class ClassTitular(models.Model):
    """Titular of a class."""

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('staff'))
    subclass = models.ForeignKey(SubClass, on_delete=models.CASCADE, verbose_name=_('subclass'))
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current, verbose_name=_('session'))

    class Meta:
        unique_together = (('staff', 'session', 'subclass'),)
        verbose_name = _('class_titular').capitalize()

