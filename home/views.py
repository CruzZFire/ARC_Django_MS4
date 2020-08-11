from django.shortcuts import render

from books.models import Book


def home(request):
    """" A view for index page """

    promoted = Book.objects.filter(promoted=True)[0:11]

    context = {
        "promoted": promoted,
    }

    return render(request, 'home/index.html', context)
