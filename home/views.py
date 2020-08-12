from django.db.models import Count
from django.shortcuts import render

from books.models import Book
from reviews.models import Review


def home(request):
    """" A view for index page """

    promoted = Book.objects.filter(promoted=True)[0:11]

    context = {
        "promoted": promoted,
    }

    return render(request, 'home/index.html', context)


def rankings(request):
    """" A view for rankings page """

    books = Book.objects.all()
    top_rw_book = books.order_by('-ratings_count')[0:5]

    top_avg_book = books.order_by('-average_rating')[0:5]

    rw_user = Review.objects.values('user__username') \
        .annotate(count=Count('user')).order_by('-count')[0:5]

    context = {
        "top_rw_book": top_rw_book,
        "top_avg_book": top_avg_book,
        "rw_user": rw_user,
    }

    return render(request, 'home/rankings.html', context)
