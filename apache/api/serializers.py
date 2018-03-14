from rest_framework import serializers
from .models import Complaint


# Create your serializers here.

class ComplaintSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance in to JSON format."""

    class Meta:
        """Meta class to map the serializer's fields with the model fields."""
        model = Complaint
        fields = ('id', 'timestamp', 'category', 'severity', 'latitude', 'longitude')
        read_only_fields = ('timestamp', 'category', 'severity', 'latitude', 'longitude')
