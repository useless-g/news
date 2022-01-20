from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('my_page/', my_page),
]