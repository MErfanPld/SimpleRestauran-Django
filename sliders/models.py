from django.db import models

# Create your models here.

class Sliders(models.Model):
    name = models.CharField(max_length=100, null=True)
    descriptions = models.TextField(blank=True, null=True)
    iamges =  models.ImageField(upload_to='sliders/', blank=True)

    def __str__(self):
        return self.name
