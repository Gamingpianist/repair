from django.contrib import admin

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'phone')
    search_fields = ('username', 'name', 'phone')
    list_filter = ('username', 'name', 'phone')


admin.site.register(UserProfile, UserProfileAdmin)
