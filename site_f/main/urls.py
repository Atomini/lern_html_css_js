from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('barber/', barber_index, name='barber_index'),
    path('barber/shop/', barber_shop, name='barber_shop'),
    path('barber/shop/item/', barber_item, name='barber_item'),
    path('barber/price/', barber_price, name='barber_price'),

    path('device/', index_device, name='index_device'),
]
