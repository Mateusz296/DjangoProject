from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']
    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        ('External information', {
            'fields': ['genre', 'released'],
            'description': 'This fields are external information!'
        }),
        ('User information', {
            'fields': ['rating', 'description'],
            'descriptions': 'This fields will be filled with user'
        })
    ]
    readonly_fields = ['created']