from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)

    prepopulated_fields = {"slug": ("title",)}


class SingerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Singer, SingerAdmin)
admin.site.register(Category, CategoryAdmin)
