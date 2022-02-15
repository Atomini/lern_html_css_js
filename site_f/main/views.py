from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# barber
def barber_index(request):
    return render(request, 'barber/index.html')


def barber_shop(request):
    return render(request, 'barber/shop.html')


def barber_price(request):
    return render(request, 'barber/price.html')


def barber_item(request):
    return render(request, 'barber/item.html')


# device
def index_device(request):
    return render(request, 'device/index.html')