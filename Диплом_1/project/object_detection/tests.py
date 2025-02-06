# object_detection/tests.py

from django.test import TestCase
from .models import ImageFeed

class ImageFeedModelTest(TestCase):
    def test_string_representation(self):
        image_feed = ImageFeed(image='test_image.jpg')
        self.assertEqual(str(image_feed), f"Image {image_feed.id} uploaded on {image_feed.created_at}")