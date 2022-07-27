from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import string


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

    def save(self, *args, **kwargs):
        if self.current:
            AcademicSession.objects.filter(current=True).update(current=False)
        else:
            pass
        super().save(*args, **kwargs)

    def get_current():
        data = AcademicSession.objects.all()

        if data.exists():
            current = data.filter(current=True)

            if current.exists(): 
                return current.get()
            else:
                current = data.last()
                current.current = True
                current.save()
                return current
        else:
            return AcademicSession.objects.create(name="NONE", current=True)


class AcademicTerm(models.Model):
    """Academic Term."""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.current:
            AcademicTerm.objects.filter(current=True).update(current=False)
        else:
            pass
        super().save(*args, **kwargs)

    def get_current():
        data = AcademicTerm.objects.all()

        if data.exists():
            current = data.filter(current=True)

            if current.exists(): 
                return current.get()
            else:
                current = data.last()
                current.current = True
                current.save()
                return current
        else:
            return AcademicTerm.objects.create(name="NONE", current=True)


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
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "SubClass"
        verbose_name_plural = "SubClasses"
        ordering = ["name"]
        unique_together = ['parent', 'name']

    def __str__(self):
        return self.parent.name + ' ' + self.name


class Person(models.Model):
    """Person."""

    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    matricule = models.CharField(max_length=16, unique=True)
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField()
    joined_date = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex=r"^[0-9]{9}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=9, blank=True
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ["lastname", "firstname", "other_name"]

    def generate_matricule(self, obj):
        """Generate matricule."""
        self.matricule = ("%c%2i%c%3i" % (
            obj.tag,
            self.joined_date.year % 1000,
            string.ascii_uppercase[obj.pk // 1000],
            obj.pk % 1000
        )).replace(' ', '0')
        self.save(update_fields=['matricule'])

