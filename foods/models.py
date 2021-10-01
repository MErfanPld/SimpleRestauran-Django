from django.db import models
from django.utils.html import format_html

# Create your models here.

class Foods(models.Model):
    FOOD_TYPE = [
        ('*', 'All'),
        ('drinks', "Drinks"),
        ('lunch', "Lunch"),
        ('dinner', "Dinner"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='foods/')
    type_food = models.CharField(max_length=50, choices=FOOD_TYPE, default="*")

    def __str__(self):
        return self.name

    def image_field(self):
        return format_html("<img width='100' height=70 style='border-radius: 5px' src='{}'>".format(self.image.url))