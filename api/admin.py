from django.contrib import admin
from .models import Customer, Ticket, Reservation

admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Reservation)