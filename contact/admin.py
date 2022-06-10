from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','car_title','city','state','create_date')
    list_display_links =  ('first_name','car_title',)
    list_filter= ('first_name','last_name','car_title','city','state','create_date')
    search_fields = ('first_name','last_name','car_title','city','state','create_date')
    list_per_page = 25
    
    

    