from django.urls import path
from . import views
from .webhooks import stripe_webhook


urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('payment_display', views.payment_display, name='payment_display'),
    path('wh/', stripe_webhook, name='stripe_webhook'),
]
