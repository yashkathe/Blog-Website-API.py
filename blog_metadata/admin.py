from django.contrib import admin

from .models import BlogMetaData

# Register your models here.

"""
I dont want to enter the route field in admin site
Hence I am prepopulating it with slugified title 
"""
class BlogMetaDataAdmin(admin.ModelAdmin):
    prepopulated_fields = { "route" : ["title"] }

admin.site.register(BlogMetaData, BlogMetaDataAdmin)