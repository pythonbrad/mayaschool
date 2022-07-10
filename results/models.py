from django.db import models
from students.models import ClassStudent
from staffs.models import ClassTeacher
from core.models import AcademicTerm

# Create your models here.


class Note(models.Model):
    class_student = models.ForeignKey(ClassStudent, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE, default=AcademicTerm.get_current)
    value = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["class_teacher__subject"]

    def __str__(self):
        return f"{self.class_student.student} {self.class_teacher.subject} {self.term} {self.value}"
