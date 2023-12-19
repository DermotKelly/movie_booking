from django.urls import path
from .views import movie_list, theater_list, create_booking

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('theaters/', theater_list, name='theater_list'),
    path('create_booking/', create_booking, name='create_booking'),
]
