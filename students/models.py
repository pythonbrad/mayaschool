from django.db import models
from core.models import AcademicSession, SubClass, Person


class Student(models.Model):
    """Student."""

    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tag = 'S'

    def __str__(self):
        return f"{self.person.surname} {self.person.firstname} {self.person.other_name} ({self.person.matricule})"

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

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subclass = models.ForeignKey(SubClass, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current)

    class Meta:
        unique_together = (('student', 'session'),)
