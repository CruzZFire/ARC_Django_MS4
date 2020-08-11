from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from books.models import Book


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_writer = models.BooleanField(default=False)
    pic_url = models.CharField(max_length=54,
                               default='missingbook.png')
    asked_books = models.ManyToManyField(Book, through='AskBook')

    def __str__(self):
        return self.user.username


class AskBook(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(user_signed_up)
def profile_creation(sender, **kwargs):
    profile = UserProfile(user=kwargs['user'])
    profile.save()
