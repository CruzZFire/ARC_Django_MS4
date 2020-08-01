from django.shortcuts import render

# Create your views here.
def profile(request):
    """" A view for index page """
    return render(request, 'home/index.html')

def user_reviews(request):
    """" A view for index page """
    return render(request, 'home/index.html')
