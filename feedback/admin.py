from django.contrib import admin

from .models import FeedBack
# Register your models here.


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('appliance', 'feeder', 'date')
    search_fields = ('appliance', 'feeder', 'date')
    list_filter = ('appliance', 'feeder', 'date')


admin.site.register(FeedBack, FeedBackAdmin)
