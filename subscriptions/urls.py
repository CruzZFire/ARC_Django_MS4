from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.subscriptions, name='subscriptions'),
    path('wh/', webhook, name='webhook'),
]
