from django.shortcuts import render
from .models import Foods
from sliders.models import Sliders

# Create your views here.

def food_list(request):
    food_list = Foods.objects.all()
    slider_list = Sliders.objects.all()
    context = {
        "food_list": food_list,
        "slider_list": slider_list,
    }
    return render(request, 'foods/food_list.html', context)


def food_detail(request, id):
    food = Foods.objects.get(id=id)
    context = {
        "food": food
    }
    return render(request, 'foods/detail.html', context)