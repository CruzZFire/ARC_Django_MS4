from django.db import models

from books.models import Book
from profiles.models import User


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews',
                             on_delete=models.CASCADE)
    datestamp = models.DateField(auto_now=True)
    review_text = models.TextField()
    rate_choice = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), ]
    rating = models.IntegerField(choices=rate_choice)
    value_count = models.IntegerField(default=0)

    def __int__(self):
        return self.review_id

    @property
    def get_total_user_rw(self):
        reader = self.user
        user_reviews_found = Review.objects.all().filter(user=reader)
        return user_reviews_found.count()

    @property
    def get_avg_user_rw(self):
        reader = self.user
        user_reviews_found = Review.objects.all().filter(user=reader)
        user_reviews_count = user_reviews_found.count()
        rw_1 = user_reviews_found.filter(rating='1').count()
        rw_2 = user_reviews_found.filter(rating='2').count()
        rw_3 = user_reviews_found.filter(rating='3').count()
        rw_4 = user_reviews_found.filter(rating='4').count()
        rw_5 = user_reviews_found.filter(rating='5').count()
        if user_reviews_count > 0:
            rating_avg = (rw_1 + rw_2*2 + rw_3*3 + rw_4*4 + rw_5*5)/user_reviews_count
        else:
            rating_avg = 'n/a'
        
        return rating_avg
