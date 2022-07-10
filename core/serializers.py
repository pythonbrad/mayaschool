from .models import (
    SystemConfig, AcademicSession, AcademicTerm,
    Subject, Class, SubClass
)
from rest_framework import serializers


class SystemConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemConfig
        exclude = []


class AcademicSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcademicSession
        exclude = []


class AcademicTermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcademicTerm
        exclude = []


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        exclude = []


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        exclude = []


class SubClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubClass
        exclude = []
