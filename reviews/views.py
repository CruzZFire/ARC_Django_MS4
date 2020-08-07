from django.shortcuts import render

from .models import Review
from books.models import Book
from profiles.models import UserProfile


def book_reviews(request, book_id):
    """" A view for all the reviews of a book """
    books = Book.objects.get(book_id=book_id)

    context = {
        "book" : books,
    }

    return render(request, 'reviews/book_reviews.html', context)


def user_reviews(request, username):
    """" A view for all the reviews made from a profile """
    user = UserProfile.objects.get(user__username=username)

    context = {
        "user" : user,
    }

    return render(request, 'reviews/user_reviews.html')