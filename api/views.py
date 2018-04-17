from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from rest_framework import generics, permissions

from .models import Complaint
from .permissions import IsOwner, IsCreationOrIsAuthenticated
from .serializers import ComplaintSerializer, UserSerializer


# Create filters here

class ComplaintFilter(filters.FilterSet):
    timestamp = filters.DateTimeFromToRangeFilter(name='timestamp')
    latitude = filters.RangeFilter(name='latitude')
    longitude = filters.RangeFilter(name='longitude')

    # time = filters.TimeRangeFilter(name='timestamp')
    # timestamp__gte = filters.DateTimeFilter(name='timestamp', lookup_expr='timestamp__gte')
    # timestamp__lte = filters.DateTimeFilter(name='timestamp', lookup_expr='timestamp__lte')

    class Meta:
        model = Complaint
        fields = ['owner', 'category', 'sub_category']


# Create views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of our REST API."""
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComplaintFilter

    def perform_create(self, serializer):
        """Save the POST data when creating a new complaint"""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the HTTP GET, PUT, and DELETE requests."""

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListCreateAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCreationOrIsAuthenticated,)

    def perform_create(self, serializer):
        """Save the POST data when creating a new complaint"""
        serializer.save()


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

#
# class ComplaintsByUser(generics.ListAPIView):
#     serializer_class = ComplaintSerializer
#
#     def get_queryset(self):
#         """This queryset should return a list of all complaints from a given user."""
#         pk = self.kwargs('pk')
#         return Complaint.objects.filter(owner=pk)
#
#
# class ComplaintsByLocation(generics.ListAPIView):
#     serializer_class = ComplaintSerializer
#
#     def get_queryset(self):
#         """This queryset should return a list of all complaints within a given area."""
#         pass
