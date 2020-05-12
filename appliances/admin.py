from django.contrib import admin

from .models import Appliance

# Register your models here.


class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Appliance, ApplianceAdmin)
