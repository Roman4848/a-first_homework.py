# object_detection/admin.py

from django.contrib import admin
from .models import ImageFeed  # Предполагается, что у вас есть модель ImageFeed

admin.site.register(ImageFeed)
