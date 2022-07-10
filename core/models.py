from django.db import models


# Create your models here.
class SystemConfig(models.Model):
    """System configuration."""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class AcademicSession(models.Model):
    """Academic Session."""

    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_current():
        current = AcademicSession.objects.filter(current=True)

        if current.exists():
            return current.get().pk
        else:
            return AcademicSession.objects.create(name="NONE").pk


class AcademicTerm(models.Model):
    """Academic Term."""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_current():
        current = AcademicTerm.objects.filter(current=True)

        if current.exists():
            return current.get().pk
        else:
            return AcademicTerm.objects.create(name="NONE").pk


class Subject(models.Model):
    """Subject."""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Class(models.Model):
    """Parent class."""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class SubClass(models.Model):
    """Child class."""

    parent = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "SubClass"
        verbose_name_plural = "SubClasses"
        ordering = ["name"]

    def __str__(self):
        return self.parent.name + ' ' + self.name
