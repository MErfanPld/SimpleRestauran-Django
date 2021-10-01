from django.shortcuts import render
from .models import Stuffs

# Create your views here.


def stuff(request):
    stuff_list = Stuffs.objects.all()
    context = {
        "stuff_list": stuff_list
    }
    return render(request, 'stuff/stuff.html', context)
