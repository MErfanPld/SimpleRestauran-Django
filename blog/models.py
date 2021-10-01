from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=True, max_length=1000)
    descriptions = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_image = models.ImageField(upload_to='blogs/', blank=True)
    second_image = models.ImageField(upload_to='blogs/', blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    tags = models.ManyToManyField("Tag", default=None, related_name="blogs", blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments")
    fullname = models.CharField(max_length=500)
    email = models.EmailField(blank=True)
    massage = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.massage