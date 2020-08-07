from django.shortcuts import render


def subscriptions(request):
    """" A view for index page """
    return render(request, 'subscriptions/subscriptions.html')
