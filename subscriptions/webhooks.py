import datetime
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

from profiles.models import User


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
        payment_intent = event.data.object

        set_sub_until(payment_intent)

    return HttpResponse(status=200)


def set_sub_until(charge):
    price = charge.amount
    email = charge.billing_details.email
    user = User.objects.get(email=email)
    today = datetime.now()

    if price == 2000:
        delta = 30
    elif price == 8000:
        delta = 182
    elif price == 10000:
        delta = 365

    finish_date = today + timedelta(days=delta)
    user.userprofile.set_subsciption_until(finish_date)

    return
