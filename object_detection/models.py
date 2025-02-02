from django.db import models
from django.contrib.auth.models import User

class ImageFeed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"
# Create your models here.
