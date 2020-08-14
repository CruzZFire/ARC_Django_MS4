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
        price=sub_instance.price,
        currency=sub_instance.currency,
    )

    context =  {
        "user_email": request.user.email,
        "client_secret": payment_intent.client_secret,
        "stripe_public": settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'subscriptions/payment_display.html', context)


@login_required
def payment_display(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']
    stripe.api_key = API_KEY

    if automatic == 'on':
        # create subs
        customer = stripe.Customer.create(
            email=request.user.email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
        s = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )
        latest_invoice = stripe.Invoice.retrieve(s.latest_invoice)

        ret = stripe.PaymentIntent.confirm(
            latest_invoice.payment_intent
        )

        if ret.status == 'requires_action':
            pi = stripe.PaymentIntent.retrieve(
                latest_invoice.payment_intent
            )
            context = {}

            context['payment_intent_secret'] = pi.client_secret
            context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY

            return render(request, 'land/payments/3dsec.html', context)
    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id
        )

    return render(request, 'land/payments/thank_you.html')
