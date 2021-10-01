from django.db import models

# Create your models here.

class Reservation(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12)
    number = models.IntegerField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, blank=True)

    def __str__(self):
        return self.fullname