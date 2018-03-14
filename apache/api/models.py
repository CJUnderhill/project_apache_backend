from django.db import models


# Create your models here.
class Complaint(models.Model):
    """This class represents the Complaint model."""
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.TextField()
    severity = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
        """This function returns a string representation of the class's contents."""
        return '%s %s %s %s %s' % (str(self.timestamp), self.category, self.severity, self.latitude, self.longitude)
