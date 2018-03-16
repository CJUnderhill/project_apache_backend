from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Complaint


# Create tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the Complaint model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="root")
        self.complaint_category = "Street Noise"
        self.complaint_severity = "5"
        self.complaint_latitude = "55.6786513"
        self.complaint_longitude = "12.5693486"
        self.complaint = Complaint(comments=self.complaint_comments,
                                   severity=self.complaint_severity,
                                   latitude=self.complaint_latitude,
                                   longitude=self.complaint_longitude,
                                   owner=user)

    def test_model_can_create_a_complaint(self):
        """Test the Complaint model can create a Complaint"""
        old_count = Complaint.objects.count()
        self.complaint.save()
        new_count = Complaint.objects.count()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(old_count + 1, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.complaint), self.complaint_category)


class ViewTestCase(TestCase):
    """Test suite for the API views."""

    def setUp(self):
        """Define the test client and other variables."""
        user = User.objects.create(username="root")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.complaint_data = {'category': 'Street Noise',
                               'severity': '5',
                               'latitude': '55.6786513',
                               'longitude': '12.5693486',
                               'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.complaint_data,
            format="json"
        )

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/complaints/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_create_a_complaint(self):
        """Test the api has complaint creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_complaint(self):
        """Test the api can get a given complaint."""
        complaint = Complaint.objects.get(id=1)
        res = self.client.get('/complaints/', kwargs={'pk': complaint.id}, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, complaint)

    def test_api_can_update_a_complaint(self):
        """Test the api can update a given complaint."""
        """Note from Chad: I don't think the actual API should be able to do this."""
        complaint = Complaint.objects.get()
        change_complaint = {'comments': 'Business Noise',
                            'severity': self.complaint_data['severity'],
                            'latitude': self.complaint_data['latitude'],
                            'longitude': self.complaint_data['longitude']}
        res = self.client.put(
            reverse('details', kwargs={'pk': complaint.id}),
            change_complaint, format='json'
        )
        print(res)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_complaint(self):
        """Test the api can delete a bucketlist."""
        complaint = Complaint.objects.get()
        res = self.client.delete(
            reverse('details', kwargs={'pk': complaint.id}),
            format='json', follow=True)

        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)
