from django.contrib import admin
from .models import Notice
# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(Notice, NoticeAdmin)