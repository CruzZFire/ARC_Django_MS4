import datetime
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from datetime import date

from books.models import Book


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_writer = models.BooleanField(default=False)
    pic_url = models.CharField(max_length=54,
                               default='missingbook.png')
    asked_books = models.ManyToManyField(Book, through='AskBook')
    sub_until = models.DateField(null=True, blank=True)

    def set_sub_until(self, date_or_times):
        if isinstance(date_or_times, int):
            sub_until = date.fromtimestamp(date_or_times)
        elif isinstance(date_or_times, str):
            sub_until = date.fromtimestamp(int(date_or_times))
        else:
            sub_until = date_or_times
        self.sub_until = sub_until
        self.save()

    def has_sub(self, current_date = datetime.date.today()):
        if self.sub_until is None:
            return False

        return current_date < self.sub_until

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
