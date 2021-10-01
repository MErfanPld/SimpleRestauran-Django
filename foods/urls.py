from django.urls import path
from .views import food_list, food_detail

app_name = "foods"

urlpatterns = [
    path('', food_list),
    path('<int:id>/', food_detail, name="detail")
]