from django.db import models


class India(models.Model):
    state = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    population = models.IntegerField()
    famous_food = models.CharField(max_length=30)
    popular_temples = models.CharField(max_length=40)
    no_of_taluka = models.IntegerField()
