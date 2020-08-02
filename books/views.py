from django.shortcuts import render
from .models import Book

def all_books(request):
    """" A view for all books page, filter and sort functions """
    
    books = Book.objects.all().order_by('title')

    context = {
        "books": books,
    }
    
    return render(request, 'books/books.html', context)

def book_detail(request):
    """" A view for index page """
    return render(request, 'home/index.html')

def add_book(request):
    """" A view for index page """
    return render(request, 'home/index.html')

def edit_book(request):
    """" A view for index page """
    return render(request, 'home/index.html')

def del_book(request):
    """" A view for index page """
    return render(request, 'home/index.html')
