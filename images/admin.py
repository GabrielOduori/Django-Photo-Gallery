from django.contrib import admin
from .models import Image, Location, Category

# Register your models here.





class ImageAdmin(admin.ModelAdmin):
    list_display = ['name','category','location','pub_date']
    ordering = ['pub_date']
    
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    
    
admin.site.register(Image, ImageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)