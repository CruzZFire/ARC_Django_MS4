from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse, get_object_or_404

from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile, AskBook
from books.models import Book
from reviews.models import Review


@login_required
def profile(request):
    """" A view for profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_reviews_found = Review.objects.filter(user_id=profile.user_id)
    user_reviews_count = user_reviews_found.count()
    user_reviews_short = user_reviews_found.order_by('-review_id')[0:3]
    short_reviews_count = user_reviews_short.count()
    books_in_profile = profile.asked_books.all()
    read_list_size = 4 - books_in_profile.count()
    empty_loop = range(0, read_list_size)

    context = {
        "profile": profile,
        "books_in_profile": books_in_profile,
        "read_list_size": read_list_size,
        "empty_loop": empty_loop,
        "user_reviews_found": user_reviews_found,
        "user_reviews_count": user_reviews_count,
        "user_reviews_short": user_reviews_short,
        "short_reviews_count": short_reviews_count,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    if not request.user.username == user_profile.user.username:
        messages.error(request, 'Sorry, that is not your profile')
        return redirect(reverse('profile'))
    
    user_form = UserUpdateForm(instance=user_profile.user)
    profile_form = ProfileUpdateForm(instance=user_profile)

    context = {
        "user_profile": user_profile,
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, 'profiles/edit_profile.html', context)


@login_required
def update_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    user_form = UserUpdateForm(request.POST or None,
                               instance=request.user)
    profile_form = ProfileUpdateForm(request.POST or None,
                                     instance=request.user.userprofile)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.success(request, 'User Updated')
        else:
            messages.error(request, 'Something was wrong with your Basic Info')
            return redirect(reverse('profile'))

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Avatar Updated')
        else:
            messages.error(request, 'Error Changing Avatar')
            return redirect(reverse('profile'))

    return redirect(reverse('profiles/profile'))


@login_required
def user_books(request, username):
    """" Manage profile books for user """
    user_profile = get_object_or_404(UserProfile, user__username=username)
    if not request.user.username == user_profile.user.username:
        messages.error(request, 'Sorry, that is not your profile')
        return redirect(reverse('profile'))

    books_in_profile = user_profile.asked_books.all()
    read_list_size = 4 - books_in_profile.count()
    empty_loop = range(0, read_list_size)

    context = {
        "books_in_profile": books_in_profile,
        "empty_loop": empty_loop,
    }

    return render(request, 'profiles/user_books.html', context)


@login_required
def ask_book(request, book_id):
    """" Get or Create books in asked-books """
    book = Book.objects.get(book_id=book_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_book_count = user_profile.asked_books.count()

    if user_profile.asked_books.filter(book_id=book.book_id):
        messages.error(request, 'Already on your read list')
    else:
        if user_book_count < 4:
            user_profile.asked_books.add(book)
            messages.success(request, 'Book added to your read list')
        else:
            messages.error(request, 'Read list full!!')

    return redirect(reverse('profile'))


@login_required
def rmv_book(request, book_id):
    """" Remove books in asked-books """
    book = Book.objects.get(book_id=book_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    user_profile.asked_books.remove(book)
    messages.success(request, 'Book removed from your read list')

    return redirect(reverse('profile'))