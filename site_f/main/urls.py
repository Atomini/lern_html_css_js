from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('barber/', barber_index, name='barber_index'),
    path('barber/shop/', barber_shop, name='barber_shop'),

    path('device/', index_device, name='index_device'),
]
