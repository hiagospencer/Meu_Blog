from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor', 'categoria', 'data')
    list_filter = ('categoria',)
    list_editable = ('categoria',)

admin.site.register(Blog, BlogAdmin)
