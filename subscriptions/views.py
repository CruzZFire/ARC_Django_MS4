import os
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import SubscriptionType


STRIPE_API_KEY = settings.STRIPE_SECRET_KEY


@require_POST
@csrf_exempt
def stripe_webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle the event
    if event.type == 'charge.succeeded':
        # object has  payment_intent attr
        set_sub_until(event.data.object)

    return HttpResponse(status=200)


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
        "sub_instance_id": sub_instance.stripe_sub_id,
        "client_secret": payment_intent.client_secret,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        "payment_intent_id": payment_intent.id,
    }

    return render(request, 'subscriptions/payment_display.html', context)


@login_required
def payment_display(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_sub_id = request.POST['sub_instance_id']
    stripe.api_key = STRIPE_API_KEY

    customer = stripe.Customer.create(
        email=request.user.email,
        payment_method=payment_method_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        }
    )

    if stripe_sub_id == os.environ.get('STRIPE_SUBSCRIPTION_ID'):
        sub = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'subscription': stripe_sub_id
                },
            ]
        )
        latest_invoice = stripe.Invoice.retrieve(sub.latest_invoice)

        ret = stripe.PaymentIntent.confirm(
            latest_invoice.payment_intent_id
        )
    else:    
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
