from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'status', 'start', 'finish']
    readonly_fields = ['status', 'start']

admin.site.register(Car)