from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()

class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    num_tickets = models.PositiveIntegerField()