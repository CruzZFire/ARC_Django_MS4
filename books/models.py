from django.db import models
from django.core.validators import MinLengthValidator


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    books_count = models.IntegerField(default=1)
    authors = models.CharField(max_length=254)
    publication_year = models.CharField(max_length=4, null=True, blank=True,
                                        validators=[MinLengthValidator(4)])
    title = models.CharField(max_length=254)
    language_code = models.CharField(max_length=5, default="eng")
    average_rating = models.DecimalField(max_digits=3, decimal_places=2,
                                         null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    ratings_1 = models.IntegerField(null=True, blank=True)
    ratings_2 = models.IntegerField(null=True, blank=True)
    ratings_3 = models.IntegerField(null=True, blank=True)
    ratings_4 = models.IntegerField(null=True, blank=True)
    ratings_5 = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    promoted = models.BooleanField(default=False)
    v_promoted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
