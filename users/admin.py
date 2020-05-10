from django.contrib import admin

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'phone', 'gender')
    search_fields = ('username', 'name', 'phone', 'gender')
    list_filter = ('username', 'name', 'phone', 'gender')


admin.site.register(UserProfile, UserProfileAdmin)
