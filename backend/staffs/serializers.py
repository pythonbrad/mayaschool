from .models import Staff
from rest_framework import serializers


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        exclude = []
        read_only_fields = [
            'matricule', 'date_of_admission'
        ]
