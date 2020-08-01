from django.shortcuts import render

# Create your views here.
def all_books(request):
    """" A view for index page """
    return render(request, 'home/index.html')

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
