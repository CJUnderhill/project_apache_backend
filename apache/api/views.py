from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import ComplaintSerializer, UserSerializer
from .models import Complaint

from django.contrib.auth.models import User


# Create views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of our REST API."""
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer ):
        """Save the POST data when creating a new complaint"""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the HTTP GET, PUT, and DELETE requests."""

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer