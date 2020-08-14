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
        self.stripe_sub_id = settings.STRIPE_ONE_YEAR_ID
        self.amount = 10000
        self.name = 'One Year Subscription'


class SubscriptionMonthly:
    def __init__(self):
        self.stripe_sub_id = settings.STRIPE_SUBSCRIPTION_ID
        self.amount = 1000
        self.name = 'Monthly Subscription'


class SubscriptionType:
    def __init__(self, sub_value):
        """
        sub_value is subscription amount (value) from form
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
    def amount(self):
        return self.subscription.amount

    @property
    def name(self):
        return self.subscription.name


def set_paid_until(charge):
    stripe.api_key = settings.STRIPE_WH_SECRET
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email

        if customer:
            sub = stripe.Subscription.retrieve(
                customer['subscriptions'].data[0].id
            )
            current_period_end = sub['current_period_end']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return False

        user.userprofile.set_sub_until(current_period_end)
