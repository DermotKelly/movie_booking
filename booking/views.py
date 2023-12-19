from django.shortcuts import render
from .models import Movie, Theater, Booking

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'booking/movie_list.html', {'movies': movies})

def theater_list(request):
    theaters = Theater.objects.all()
    return render(request, 'booking/theater_list.html', {'theaters': theaters})

def create_booking(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        theater_id = request.POST.get('theater')
        user_name = request.POST.get('user_name')
        num_tickets = request.POST.get('num_tickets')

        movie = Movie.objects.get(pk=movie_id)
        theater = Theater.objects.get(pk=theater_id)

        Booking.objects.create(
            movie=movie,
            theater=theater,
            user_name=user_name,
            num_tickets=num_tickets
        )

    movies = Movie.objects.all()
    theaters = Theater.objects.all()

    return render(request, 'booking/create_booking.html', {'movies': movies, 'theaters': theaters})

