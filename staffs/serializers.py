from .models import Staff, ClassTeacher
from rest_framework import serializers


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        exclude = []
        read_only_fields = [
            'matricule', 'date_of_admission'
        ]


class ClassTeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassTeacher
        exclude = []
        read_only_fields = [
            'session'
        ]