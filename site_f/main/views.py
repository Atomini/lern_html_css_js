from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'barber/index.html')


def index_device(request):
    return render(request, 'device/index.html')