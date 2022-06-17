from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
import string


class Student(models.Model):
    """Student."""

    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    matricule = models.CharField(max_length=16, unique=True)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField()
    date_of_admission = models.DateTimeField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex=r"^[0-9]{9}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=9, blank=True
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["surname", "firstname", "other_name"]

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name} ({self.matricule})"

    def generate_matricule(self, tag):
        """Generate matricule."""
        self.matricule = ("%c%2i%c%3i" % (
            tag,
            self.date_of_admission.year % 1000,
            string.ascii_uppercase[self.pk // 1000],
            self.pk % 1000
        )).replace(' ', '0')
        self.save(update_fields=['matricule'])

    def save(self, *args, **kwargs):
        """Save."""
        super().save(*args, **kwargs)
        if not self.matricule:
            self.generate_matricule('S')
        else:
            pass
