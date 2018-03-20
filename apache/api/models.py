from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create models here.

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/<complaint_timestamp>.jpg
    return 'images/{0}'.format(str(instance.timestamp) + ".jpg")


def audio_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/audio/<complaint_timestamp>.aac
    return 'audio/{0}'.format(str(instance.timestamp) + ".aac")


class Complaint(models.Model):
    """This class represents the Complaint model."""

    SEVERITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    category = models.TextField(blank=True)  # blank=True means field is not required
    severity = models.IntegerField(choices=SEVERITY_CHOICES, default=3)
    latitude = models.TextField()  # TODO Ensure latitude is within acceptable range
    longitude = models.TextField()  # TODO Ensure longitude is within acceptable range
    image = models.ImageField(upload_to=image_directory_path, blank=True)  # blank=True means field is not required
    audio = models.FileField(upload_to=audio_directory_path, blank=True)  # blank=True means field is not required
    owner = models.ForeignKey('auth.User', related_name='complaints', on_delete=models.CASCADE)

    def __str__(self):
        """This function returns a string representation of the class's contents."""
        return "{}".format(str(self.severity))
        # return '%s %s %s %s %s' % (str(self.timestamp), self.category, self.severity, self.latitude, self.longitude)


# This receiver handles token creation immediately after a user is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
