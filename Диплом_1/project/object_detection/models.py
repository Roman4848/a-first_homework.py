# object_detection/models.py

from django.db import models

class ImageFeed(models.Model):
    image = models.ImageField(upload_to='images/')
    processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded on {self.created_at}"