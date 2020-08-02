from django.shortcuts import render

# Create your views here.
def home(request):
    """" A view for index page """

    context = {
        
    }

    return render(request, 'home/index.html', context)
