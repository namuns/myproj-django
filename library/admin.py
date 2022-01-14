from django.contrib import admin
from library.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']