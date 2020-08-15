import os
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import SubscriptionType


STRIPE_API_KEY = settings.STRIPE_SECRET_KEY


def subscriptions(request):
    """" A view for subscription offers page """

    return render(request, 'subscriptions/subscriptions.html')


@login_required
def payment_process(request):
    """" A view for processing form data payment """
    stripe.api_key = STRIPE_API_KEY
    subscription = request.POST.get('subscription')

    sub_instance = SubscriptionType(sub_value=subscription)

    payment_intent = stripe.PaymentIntent.create(
        amount=sub_instance.amount,
        currency=sub_instance.currency,
        payment_method_types=['card']
    )

    context =  {
        "user_email": request.user.email,
        "sub_instance": sub_instance,
        "stripe_sub_id": sub_instance.stripe_sub_id,
        "client_secret": payment_intent.client_secret,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        "payment_intent_id": payment_intent.id,
    }

    return render(request, 'subscriptions/payment_display.html', context)


@login_required
def payment_display(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_sub_id = request.POST['stripe_sub_id']
    stripe.api_key = STRIPE_API_KEY

    customer = stripe.Customer.create(
        email=request.user.email,
        payment_method=payment_method_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        }
    )

    stripe.PaymentIntent.modify(
        payment_intent_id,
        payment_method=payment_method_id,
        customer=customer.id
    )

    ret = stripe.PaymentIntent.confirm(
        payment_intent_id
    )

    if ret.status == 'requires_action':
        payment_intent = stripe.PaymentIntent.retrieve(
            payment_intent_id
        )
        context = {
            "payment_intent_secret": payment_intent.client_secret,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        }

        return render(request, 'subscriptions/3dsecure.html', context)

    return render(request, 'subscriptions/sub_success.html')
