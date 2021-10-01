from django.urls import path
from .views import Countact_us

urlpatterns = [
    path('contact-us/', Countact_us)
]