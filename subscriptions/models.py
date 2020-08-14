import stripe
from django.db import models
from django.conf import settings


class SubscriptionOneMonth:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_ONE_MONTH_ID
        self.price = 2000


class SubscriptionOneYear:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_ONE_YEAR_ID
        self.price = 10000


class SubscriptionMonthly:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_SUBSCRIPTION_ID
        self.price = 1000


class SubscriptionType:
    def __init__(self, sub_value):
        """
        sub_value is subscription price (value) from form
        """
        if sub_value == 'onemonth':
            self.subscription = SubscriptionOneMonth()
            self.id = 'onemonth'
        elif sub_value == 'oneyear':
            self.subscription = SubscriptionOneYear()
            self.id = 'oneyear'
        elif sub_value == 'monthly':
            self.subscription = SubscriptionMonthly()
            self.id = 'monthly'
        else:
            raise ValueError('Invalid sub_value value')

        self.currency = 'EUR'

    @property
    def stripe_sub_id(self):
        return self.subscription.stripe_sub_id

    @property
    def price(self):
        return self.subscription.price
