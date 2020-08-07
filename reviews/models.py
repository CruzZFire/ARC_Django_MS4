from django.db import models

from books.models import Book
from profiles.models import User


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    datestamp = models.DateField(auto_now=True)
    review_text = models.TextField()
    rate_choice = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),]
    rating = models.IntegerField(choices=rate_choice)
    value_count = models.IntegerField(default=0)


    def __str__(self):
        return self.review_id