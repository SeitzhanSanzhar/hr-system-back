from django.contrib import admin
from .models import Staff, StaffToPosition, Position

# Register your models here.

admin.site.register(Staff)
admin.site.register(StaffToPosition)
admin.site.register(Position)