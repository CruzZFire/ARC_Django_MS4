import stripe
from django.db import models
from django.conf import settings


class SubscriptionOneMonth:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_ONE_MONTH_ID
        self.amount = 2000
        self.name = 'One Month Subscription'


class SubscriptionOneYear:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_HALF_YEAR_ID
        self.amount = 8000
        self.name = 'Half Year Subscription'


class SubscriptionMonthly:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_ONE_YEAR_ID
        self.amount = 10000
        self.name = 'One Year Subscription'


class SubscriptionType:
    def __init__(self, sub_value):
        """
        sub_value is subscription amount (value) from form
        """
        if sub_value == 'onemonth':
            self.subscription = SubscriptionOneMonth()
            self.id = 'onemonth'
        elif sub_value == 'halfyear':
            self.subscription = SubscriptionOneYear()
            self.id = 'halfyear'
        elif sub_value == 'oneyear':
            self.subscription = SubscriptionMonthly()
            self.id = 'oneyear'
        else:
            raise ValueError('Invalid sub_value value')

        self.currency = 'EUR'

    @property
    def stripe_sub_id(self):
        return self.subscription.stripe_sub_id

    @property
    def amount(self):
        return self.subscription.amount

    @property
    def name(self):
        return self.subscription.name
