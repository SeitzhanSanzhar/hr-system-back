from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from .view import get_all_stuff, search_staff, get_staff
=======
from .view import get_all_stuff, search_staff, get_stuff
>>>>>>> f23188d693b324ca782761b536882643ef99e96d

urlpatterns = [
    path('people/', get_all_stuff),
    path('search/', search_staff),
<<<<<<< HEAD
    path('people/<int:pk>/', get_staff),
=======
    path('view_staff/', get_stuff),
>>>>>>> f23188d693b324ca782761b536882643ef99e96d
]
