from .models import Student, ClassStudent
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        exclude = []
        read_only_fields = [
            'matricule', 'date_of_admission'
        ]


class ClassStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassStudent
        exclude = []
        read_only_fields = [
            'session'
        ]
