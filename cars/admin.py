from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Team Image'
    
    list_display = ('is_featured','thumbnail','color','model', 'state', 'created_date','body_style','transmission')
    list_display_links = ('model', 'state', 'created_date','body_style','transmission')
    search_fields = ('model', 'state', 'created_date','body_style','transmission')
    list_filter = ('model', 'state', 'created_date','body_style','transmission','doors')
    list_editable = ('is_featured',)