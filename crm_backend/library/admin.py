from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'level', 'child_count', 'get_full_path')
    search_fields = ('name', 'description')