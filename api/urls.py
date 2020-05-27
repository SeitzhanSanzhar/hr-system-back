from django.contrib import admin
from django.urls import path
from .view import get_all_stuff, search_staff, get_staff

urlpatterns = [
    path('people/', get_all_stuff),
    path('search/', search_staff),
    path('people/<int:pk>/', get_staff),
]
