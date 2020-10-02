from django.contrib import admin
from .models import Author, Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Книги"""
    list_display = ("title", "year", "country")
    list_filter = ("title", "author", "country")
    search_fields = ("title", "author")
    fieldsets = (
        (None, {
            "fields": (("title", "year"),)
        }),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("author",),)
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Авторы"""
    list_display = ("name", "age", "url")
    list_filter = ("name", "age",)
    search_fields = ("name",)
    fieldsets = (
        (None, {
            "fields": (("name", "age"),)
        }),
        (None, {
            "fields": ("description", "url")
        }),
    )
