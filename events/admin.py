from django.contrib import admin

# Register your models here.
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_day','event_title','event_manager','draft','pub_date','contact_num')
    list_display_links = ('event_title',)
    list_filter = ('event_day','pub_date','event_manager')
    list_editable = ('draft','event_day',)
    search_fields = ('event_title',)
    prepopulated_fields = {'slug' : ('event_title',)}

admin.site.register(models.Events,EventAdmin)