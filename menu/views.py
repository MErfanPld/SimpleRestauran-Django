from django.shortcuts import render
from foods.models import Foods

# Create your views here.

def menu(request):
    food_list = Foods.objects.all()
    context = {
        "food_list" : food_list
    }
    return render(request, "menu/menu.html", context)