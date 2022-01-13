from django.contrib import admin
from library.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]