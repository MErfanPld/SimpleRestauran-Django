from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100, blank=True)
    little_story = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='about/', blank=True)

    def __str__(self):
        return self.title