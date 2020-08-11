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

    @property
    def get_reviews(self):
        book_rw_short = self.reviews.all().order_by('-review_id')[0:3]
        return book_rw_short

    @property
    def get_avg_book_rw(self):
        book_rw_object = self.reviews.all()
        book_rw_all = book_rw_object.count() + self.ratings_count
        rw_1 = book_rw_object.filter(rating='1').count() + self.ratings_1
        rw_2 = book_rw_object.filter(rating='2').count() + self.ratings_2
        rw_3 = book_rw_object.filter(rating='3').count() + self.ratings_3
        rw_4 = book_rw_object.filter(rating='4').count() + self.ratings_4
        rw_5 = book_rw_object.filter(rating='5').count() + self.ratings_5

        if book_rw_all > 0:
            book_rw_avg = (rw_1+rw_2*2+rw_3*3+rw_4*4+rw_5*5)/book_rw_all
        else:
            book_rw_avg = 'n/a'
        
        return book_rw_avg
