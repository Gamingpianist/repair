from django.contrib import admin

from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'price', 'appliance', 'name', 'address')
    search_fields = ('status', 'price', 'appliance', 'name', 'address')
    list_filter = ('status', 'price', 'appliance', 'name', 'address')


admin.site.register(Order, OrderAdmin)
