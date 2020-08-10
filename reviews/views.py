from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404

from .forms import ReviewForm
from .models import Review
from books.models import Book
from profiles.models import UserProfile


@login_required
def book_reviews(request, book_id):
    """" A view for all the reviews of a book """
    book = Book.objects.get(book_id=book_id)
    book_reviews_found = Review.objects.filter(
                         book_id=book_id).order_by('-review_id')
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.book = book
            form.save()
            messages.success(request, 'Review Submitted')
            form = ReviewForm(None)

    context = {
        "book": book,
        "book_reviews_found": book_reviews_found,
        "form": form,
    }

    return render(request, 'reviews/book_reviews.html', context)


@login_required
def user_reviews(request, username):
    """" A view for all the reviews made from a profile """
    user_reviews_found = Review.objects.filter(user__username=username)
    if user_reviews_found:
        user_reviews_data = user_reviews_found[0]
    else:
        user_reviews_data = ''
    user_reviews_by_time = user_reviews_found.order_by('-review_id')
    reviewer = UserProfile.objects.get(user__username=username)

    context = {
        "reviewer": reviewer,
        "user_reviews_data": user_reviews_data,
        "user_reviews_found": user_reviews_found,
        "user_reviews_by_time": user_reviews_by_time,
    }

    return render(request, 'reviews/user_reviews.html', context)


@login_required
def edit_review(request, review_id):
    """ Delete a review from the page """
    review_found = get_object_or_404(Review, pk=review_id)
    if not request.user.username == review_found.user.username:
        messages.error(request, 'Sorry, only the reviewer can do that')
        return redirect(reverse('profile'))

    review_found.delete()
    messages.success(request, 'Review Edited and Published')
    return redirect(reverse('home'))


@login_required
def delete_review(request, review_id):
    """ Delete a review from the page """
    review_found = get_object_or_404(Review, pk=review_id)
    if not request.user.username == review_found.user.username:
        messages.error(request, 'Sorry, just the reviewer delete the review')
        return redirect(reverse('profile'))

    review_found.delete()
    messages.success(request, 'Review Deleted Succesfully!')
    return redirect(reverse('profile'))
