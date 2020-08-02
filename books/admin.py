from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "book_id",
        "books_count",
        "authors",
        "publication_year",
        "language_code",
        "title",
        "average_rating",
        "ratings_count",
        "ratings_1",
        "ratings_2",
        "ratings_3",
        "ratings_4",
        "ratings_5",
        "image_url",
    )
    ordering = ("title",)


admin.site.register(Book, BookAdmin)