from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organizer',
        'start_date',
        'end_date',
        'is_approved',
    )

