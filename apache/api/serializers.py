from rest_framework import serializers
from .models import Complaint


# Create serializers here.

class ComplaintSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance in to JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map the serializer's fields with the model fields."""
        model = Complaint
        fields = ('id', 'timestamp', 'owner', 'category', 'severity', 'latitude', 'longitude',)
        read_only_fields = ('timestamp',)
        # read_only_fields = ('timestamp', 'category', 'severity', 'latitude', 'longitude')
