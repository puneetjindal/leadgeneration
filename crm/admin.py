from django.contrib import admin
from crm.models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = ()
    list_display = ('name', 'website','primary_owner')
    list_filter = ['name', 'primary_owner']

admin.site.register(Client, ClientAdmin)