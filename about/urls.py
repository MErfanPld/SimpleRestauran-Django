from django.urls import path
from .views import About_us

urlpatterns = [
    path('about-us/', About_us),
]