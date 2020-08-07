from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review
from books.models import Book
from profiles.models import UserProfile


@login_required
def book_reviews(request, book_id):
    """" A view for all the reviews of a book """
    books = Book.objects.get(book_id=book_id)
    book_reviews_found = Review.objects.filter(book_id=book_id)
    form = ReviewForm(request.POST or None)

    context = {
        "book": books,
        "book_reviews_found": book_reviews_found,
        "form": form,
    }

    return render(request, 'reviews/book_reviews.html', context)


@login_required
def user_reviews(request, username):
    """" A view for all the reviews made from a profile """
    user = UserProfile.objects.get(user__username=username)
    user_reviews_found = Review.objects.filter(user__username=username)
    user_reviews_by_time = user_reviews_found.order_by('-datestamp')

    context = {
        "user": user,
        "user_reviews_found": user_reviews_found,
        "user_reviews_by_time": user_reviews_by_time,
    }

    return render(request, 'reviews/user_reviews.html', context)
