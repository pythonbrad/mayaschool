from .models import (
    SystemConfig, AcademicSession, AcademicTerm,
    Subject, Class, SubClass
)
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    SystemConfigSerializer, AcademicSessionSerializer, AcademicTermSerializer,
    SubjectSerializer, ClassSerializer, SubClassSerializer
)


class SystemConfigViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = SystemConfig.objects.all().order_by('-key')
    serializer_class = SystemConfigSerializer
    permission_classes = [permissions.IsAuthenticated]


class AcademicSessionViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = AcademicSession.objects.all().order_by('-name')
    serializer_class = AcademicSessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AcademicTermViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = AcademicTerm.objects.all().order_by('-name')
    serializer_class = AcademicTermSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Subject.objects.all().order_by('-name')
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClassViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Class.objects.all().order_by('-name')
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubClassViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = SubClass.objects.all().order_by('-parent', '-name')
    serializer_class = SubClassSerializer
    permission_classes = [permissions.IsAuthenticated]
