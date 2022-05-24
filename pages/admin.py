from django.contrib import admin
from .models import Client

class Clients(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'start_date' )
    list_display_links = ('id', 'payment_id')
    search_field = ('payment_id',)

admin.site.register(Client, Clients)