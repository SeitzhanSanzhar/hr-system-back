from django.contrib import admin
from django.urls import path
from .view import get_all_stuff

urlpatterns = [
    path('people/', get_all_stuff),
]
