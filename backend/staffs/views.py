from .models import Staff
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Staff.objects.all().order_by('-matricule')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]
