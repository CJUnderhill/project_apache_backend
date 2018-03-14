from django.test import TestCase

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
