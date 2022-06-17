from .models import Student
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Student.objects.all().order_by('-matricule')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
