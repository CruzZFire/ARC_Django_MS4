from django.shortcuts import render

# Create your views here.
def home(request):
    """" A view for index page """
    return render(request, 'home/index.html')
