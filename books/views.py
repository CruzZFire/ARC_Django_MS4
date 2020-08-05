from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Book


def all_books(request):
    """" A view for all books page, filter and sort functions """
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


def book_detail(request, book_id):
    """" A view for book detail page """
    book = get_object_or_404(Book, pk=book_id)

    context = {
        "book": book,
    }

    return render(request, 'books/book_detail.html', context)


def add_book(request):
    """" A view for index page """
    return render(request, 'home/index.html')


def edit_book(request, book_id):
    """" A view for index page """
    return render(request, 'home/index.html')


def del_book(request, book_id):
    """" A view for index page """
    return render(request, 'home/index.html')
