from django.shortcuts import redirect, render, get_object_or_404
from .models import UserProfile
from books.models import Book


def add_to_books(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    redirect_url = request.POST.get('redirect_url')
    owned_books = UserProfile.asked_books

    if book_id in list(owned_books.keys()):
        messages.error(request, f'Book {book.title} already on your asked books')
    else:
        owned_books.append({book_id: book.image_url})

    UserProfile.asked_books = owned_books
    return redirect(redirect_url)


def profile(request):
    """" A view for profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        "user": profile,
    }

    return render(request, 'profiles/profile.html', context)

def user_reviews(request):
    """" A view for index page """
    return render(request, 'home/index.html')
