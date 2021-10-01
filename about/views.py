from django.shortcuts import render
from .models import About

# Create your views here.

def About_us(request):
    about_list = About.objects.all()
    context = {
        "about_list": about_list
    }
    return render(request, 'about/about.html', context)