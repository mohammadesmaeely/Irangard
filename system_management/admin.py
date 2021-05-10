from django.contrib import admin
from system_management.models import Ticket, State, City


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ('id', 'title')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = State
    list_display = ('id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('id', 'state', 'name')
