from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from books.models import Book


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    asked_books = models.ManyToManyField(Book, through='AskBook')
    asked_books_count = str(3)

    def __str__(self):
        return self.user.username


class AskBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


@receiver(user_signed_up)
def profile_creation(sender, **kwargs):
    profile = UserProfile(user=kwargs['user'])
    profile.save()
