from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('device/', index_device, name='index_device'),
]