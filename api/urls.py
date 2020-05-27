from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .view import get_all_stuff, search_staff, get_staff, get_stuff


urlpatterns = [
    path('people/', get_all_stuff),
    path('search/', search_staff),
    path('people/<int:pk>/', get_staff),
    path('view_staff/', get_stuff),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)