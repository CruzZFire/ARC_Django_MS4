from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Book
from reviews.forms import ReviewForm
from reviews.models import Review


def all_books(request):
    """" A view for all books page, search/filter function """
    books = Book.objects.all().order_by('title')

    paginator = Paginator(books, 24)
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        paginated_books = paginator.page(page)
    except PageNotAnInteger:
        paginated_books = paginator.page(1)
    except EmptyPage:
        paginated_books = paginator.page(paginator.num_pages)

    context = {
        "paginated_books": paginated_books,
        "page_request": page_request,
    }

    return render(request, 'books/books.html', context)


def search_books(request):
    """" A view for searched books """
    books = Book.objects.all().order_by('title')
    query = request.GET.get('book_search')
    if query:
        search_books = books.filter(
            Q(title__icontains=query) |
            Q(authors__icontains=query)
        ).distinct()

    results = search_books.count()

    context = {
        "search_books": search_books,
        "results": results,
        "query": query,
    }

    return render(request, 'books/book_search.html', context)


def book_detail(request, book_id):
    """" A view for book detail page """
    book = get_object_or_404(Book, pk=book_id)
    book_reviews_found = Review.objects.filter(
                         book_id=book_id).order_by('-review_id')
    if book_reviews_found.count() > 0:
        book_reviews_count = book_reviews_found.count() + book.ratings_count
    else:
        book_reviews_count = book.ratings_count

    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.book = book
            form.save()
            messages.success(request, 'Review Submitted')
            form = ReviewForm(None)
            return redirect(reverse('book_detail', kwargs={
                'book_id': book.book_id
            }))

    context = {
        "book": book,
        "book_reviews_count": book_reviews_count,
        "form": form,
    }

    return render(request, 'books/book_detail.html', context)
