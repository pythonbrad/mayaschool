from django.db import models
from core.models import AcademicSession, Subject, SubClass, Person


class Staff(models.Model):
    """Staff."""

    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tag = 'P'


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

    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subclass = models.ForeignKey(SubClass, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current)

    class Meta:
        unique_together = (('teacher', 'session', 'subject', 'subclass'),)
