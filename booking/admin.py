from django.contrib import admin
from .models import Booking, Movie, Theater

# Register your models here.

admin.site.register(Booking)
admin.site.register(Movie)
admin.site.register(Theater)