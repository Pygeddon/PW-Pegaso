from django.contrib import admin
from TicketStore.models import Event, Organizer, AvailableDates, TypeOfEvent
# Register your models here.

class AvailableDatesInline(admin.TabularInline):
    model = AvailableDates
    extra = 1
    ordering = ['date_from'] 

class EventAdmin(admin.ModelAdmin):
    inlines = [AvailableDatesInline]
    ordering = ['event_date']

class EventTypeInline(admin.TabularInline):
    model = TypeOfEvent
    extra = 1
    ordering = ['date_from'] 

admin.site.register(Event,EventAdmin)
admin.site.register(Organizer)
admin.site.register(AvailableDates)
admin.site.register(TypeOfEvent)


