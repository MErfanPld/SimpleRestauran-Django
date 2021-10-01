from django.contrib import admin
from .models import Reservation

# Register your models here.

#=====================ReservationAdmin=====================

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("fullname", "phone", "date", "time")
    list_filter = ("date",)
    search_fields = ("fullname", "phone", "date", "time")
    ordering = ("fullname", "phone", "date", "time")

admin.site.register(Reservation,ReservationAdmin),