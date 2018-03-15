from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Complaint


# Create serializers here.

class ComplaintSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance in to JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map the serializer's fields with the model fields."""
        model = Complaint
        fields = ('id', 'timestamp', 'owner', 'category', 'severity', 'latitude', 'longitude', 'image', 'audio',)
        read_only_fields = ('timestamp',)
        # read_only_fields = ('timestamp', 'category', 'severity', 'latitude', 'longitude')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    complaints = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Complaint.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'complaints')
