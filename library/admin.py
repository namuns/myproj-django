from django.contrib import admin
from library.models import Library


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

