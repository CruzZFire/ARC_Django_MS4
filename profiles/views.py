from django.shortcuts import redirect, render, reverse, get_object_or_404

from .models import UserProfile
from books.models import Book
from reviews.models import Review


def profile(request):
    """" A view for profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_reviews_found = Review.objects.filter(user_id=profile.user_id)
    user_reviews_count = user_reviews_found.count()
    user_reviews_short = user_reviews_found.order_by('-review_id')[0:3]
    short_reviews_count = user_reviews_short.count()

    context = {
        "profile": profile,
        "user_reviews_found": user_reviews_found,
        "user_reviews_count": user_reviews_count,
        "user_reviews_short": user_reviews_short,
        "short_reviews_count": short_reviews_count,
    }

    return render(request, 'profiles/profile.html', context)


def ask_book(request, book_id):
    """" Get or Create books in asked-books """

    return render(request, 'home/index.html')
