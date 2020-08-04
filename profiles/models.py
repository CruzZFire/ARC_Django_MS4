from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(user_signed_up)
def profile_creation(sender, **kwargs):
    profile = UserProfile(user = kwargs['user'])
    profile.save()
