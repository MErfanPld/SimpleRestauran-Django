from django.db import models

# Create your models here.

class Stuffs(models.Model):
    fullname = models.CharField(max_length=200)
    offer = models.CharField(max_length=200)
    face_book = models.URLField(blank=True)
    gmail = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    image = models.ImageField(upload_to='stuff/', blank=True)

    def __str__(self):
        return self.fullname