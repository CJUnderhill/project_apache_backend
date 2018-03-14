from django.shortcuts import render
from rest_framework import generics
from .serializers import ComplaintSerializer
from .models import Complaint


# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of our REST API."""
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def perform_create(self, serializer):
        """Save the POST data when creating a new complaint"""
        serializer.save()
