from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import string


# Create your models here.
class SystemConfig(models.Model):
    """System configuration."""

    key = models.SlugField(unique=True, verbose_name=_('key'))
    value = models.CharField(max_length=200, verbose_name=_('value'))

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = _('system_config').capitalize()


class AcademicSession(models.Model):
    """Academic Session."""

    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
    current = models.BooleanField(default=True, verbose_name=_('current'))

    class Meta:
        ordering = ["-name"]
        verbose_name = _('academic_session').capitalize()

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

    name = models.CharField(max_length=20, unique=True, verbose_name=_('name'))
    current = models.BooleanField(default=True, verbose_name=_('current'))

    class Meta:
        ordering = ["name"]
        verbose_name = _('academic_term').capitalize()

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


class Module(models.Model):
    """Module."""

    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
    code = models.CharField(max_length=16, unique=True, verbose_name=_('code'))

    class Meta:
        ordering = ["code"]
        verbose_name = _('module').capitalize()

    def __str__(self):
        return self.code


class Subject(models.Model):
    """Subject."""

    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))
    code = models.CharField(max_length=16, unique=True, verbose_name=_('code'))
    coef = models.PositiveIntegerField(default=1, verbose_name=_('coef'))
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name=_('group'))

    class Meta:
        ordering = ["code"]
        verbose_name = _('subject').capitalize()

    def __str__(self):
        return self.code


class Class(models.Model):
    """Parent class."""

    name = models.CharField(max_length=200, unique=True, verbose_name=_('name'))

    class Meta:
        verbose_name = _("class").capitalize()
        verbose_name_plural = _("classes").capitalize()
        ordering = ["name"]

    def __str__(self):
        return self.name


class SubClass(models.Model):
    """Child class."""

    parent = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_('parent'))
    name = models.CharField(max_length=200, verbose_name=_('name'))

    class Meta:
        verbose_name = _("subclass").capitalize()
        verbose_name_plural = _("subclasses").capitalize()
        ordering = ["name"]
        unique_together = ['parent', 'name']

    def __str__(self):
        return self.parent.name + ' ' + self.name


class Person(models.Model):
    """Person."""

    STATUS_CHOICES = [("active", _("active").capitalize()), ("inactive", _("inactive").capitalize())]

    GENDER_CHOICES = [("male", _("male").capitalize()), ("female", _("female").capitalize())]

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active", verbose_name=_("status")
    )
    matricule = models.CharField(max_length=16, unique=True, verbose_name=_("matricule"))
    lastname = models.CharField(max_length=200, verbose_name=_("lastname"))
    firstname = models.CharField(max_length=200, verbose_name=_("firstname"))
    other_name = models.CharField(max_length=200, blank=True, verbose_name=_("othername"))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name=_("gender"))
    date_of_birth = models.DateField()
    joined_date = models.DateField(default=timezone.now, verbose_name=_("joined_date"))

    mobile_num_regex = RegexValidator(
        regex=r"^[0-9]{9}$",
        # Translators: We want inform the user that the mobile number don't respect the format
        message=_("wrong_mobile_number").capitalize()
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=9, blank=True, verbose_name=_("mobile_number")
    )

    address = models.TextField(blank=True, verbose_name=_("address"))
    others = models.TextField(blank=True, verbose_name=_("others"))
    passport = models.ImageField(blank=True, upload_to="students/passports/", verbose_name=_("passport"))
    email = models.EmailField(blank=True, verbose_name=_("email"))

    class Meta:
        ordering = ["lastname", "firstname", "other_name"]
        verbose_name = _("person").capitalize()

    def generate_matricule(self, obj):
        """Generate matricule."""
        self.matricule = ("%c%2i%c%3i" % (
            obj.tag,
            self.joined_date.year % 1000,
            string.ascii_uppercase[obj.pk // 1000],
            obj.pk % 1000
        )).replace(' ', '0')
        self.save(update_fields=['matricule'])

