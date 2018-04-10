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
        fields = ('id', 'timestamp', 'owner', 'comments', 'category', 'sub_category',
                  'latitude', 'longitude', 'image', 'audio',)
        read_only_fields = ('timestamp',)
        # read_only_fields = ('timestamp', 'comments', 'severity', 'latitude', 'longitude')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    complaints = serializers.PrimaryKeyRelatedField(many=True, queryset=Complaint.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'complaints')

    def create(self, validated_data):
        """This will create a new user and store their information in the database."""
        validated_data['complaints'] = []  # Ensures nobody can assign complaints to users before they've submitted any

        user = super().create(validated_data)
        user.complaints.set([])
        user.set_password(validated_data['password'])
        user.save()
        return user
