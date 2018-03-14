from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Complaint


# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the Complaint model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.complaint_category = "Street Noise"
        self.complaint_severity = "5"
        self.complaint_latitude = "55.6786513"
        self.complaint_longitude = "12.5693486"
        self.complaint = Complaint(category=self.complaint_category,
                                   severity=self.complaint_severity,
                                   latitude=self.complaint_latitude,
                                   longitude=self.complaint_longitude)

    def test_model_can_create_a_complaint(self):
        """Test the Complaint model can create a Complaint"""
        old_count = Complaint.objects.count()
        self.complaint.save()
        new_count = Complaint.objects.count()
        self.assertEqual(old_count + 1, new_count)


class ViewTestCase(TestCase):
    """Test suite for the API views."""

    def setUp(self):
        """Define the test client and other variables."""
        self.client = APIClient()
        self.complaint_data = {'category': 'Street Noise',
                               'severity': '5',
                               'latitude': '55.6786513',
                               'longitude': '12.5693486'}
        self.response = self.client.post(
            reverse('create'),
            self.complaint_data,
            format="json"
        )

    def test_api_can_create_a_complaint(self):
        """Test the api has complaint creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_complaint(self):
        """Test the api can get a given complaint."""
        complaint = Complaint.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': complaint.id}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, complaint)

    def test_api_can_update_a_complaint(self):
        """Test teh api can update a given complaint."""
        """Note from Chad: I don't think the actual API should be able to do this."""
        complaint = Complaint.objects.get()
        change_complaint = {'severity': '10'}
        res = self.client.put(
            reverse('details', kwargs={'pk': complaint.id}),
            change_complaint, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_complaint(self):
        """Test the api can delete a bucketlist."""
        complaint = Complaint.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': complaint.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
