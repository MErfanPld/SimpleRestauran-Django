from django.urls import path
from .views import stuff

urlpatterns = [
    path('stuff/', stuff)
]