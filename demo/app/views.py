from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'message': 'example1',
    }
    return render(request, 'base_app.html', context)
