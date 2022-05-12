from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.photo.url))

    thumbnail.short_description = 'Team Image'
    
    list_display = ('id','thumbnail','first_name', 'designation', 'created_date')
    list_display_links = ('first_name', 'created_date')
    search_fields = ('first_name', 'designation')
    list_filter = ('designation',)

"""
NB: we want to have image display on the admin dashboard
sod we need to import format_html
from django.utils.html import format_html

the we create a function inside the model, with self and all the object
self, referring to the class and object, mean all the object

def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

.. then we can display those images on the admin panel

to change the name being display on the admin panel

thumbnail.short_description = 'Team Image'

"""
