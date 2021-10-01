from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    massage = models.TextField(blank=True)

    def __str__(self):
        return self.fullname