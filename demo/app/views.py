from django.http import HttpResponse
from django.shortcuts import render
from .models import RandomContent


def get_count():
    """
    Fetch the latest count value
    :return:
    """
    obj = RandomContent.objects.first()
    if obj:
        return obj.count
    else:
        return 0


def increment_count():
    """
    Increment count on each click
    :return:
    """
    obj = RandomContent.objects.first()
    if obj:
        obj.count += 1
        obj.save()
        return True
    else:
        return False


# Create your views here.
def index(request):
    context = {
        'count': get_count(),
    }
    if request.method == 'POST':
        increment_count()
    return render(request, 'base_app.html', context)
