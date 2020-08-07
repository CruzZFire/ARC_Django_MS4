from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import UserProfile
from books.models import Book


def profile(request):
    """" A view for profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        "profile": profile,
    }

    return render(request, 'profiles/profile.html', context)


def ask_book(request, book_id):
    """" Get or Create books in asked-books """

    return render(request, 'home/index.html')
