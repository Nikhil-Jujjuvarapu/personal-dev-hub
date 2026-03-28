from django.db import models

# Create your models here.

class StreamPlatformDetails(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
class MoviesDetails(models.Model):
    movie_name = models.CharField(max_length=10)
    release_year = models.IntegerField()
    language = models.CharField(max_length=10)
    platform = models.ForeignKey(StreamPlatformDetails,on_delete=models.CASCADE,related_name='movies',null=True,blank=True)

    def __str__(self):
        return self.movie_name

class StreamPlatformDetails1(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    
    
class MoviesDetails1(models.Model):
    movie_name = models.CharField(max_length=10)
    release_year = models.IntegerField()
    language = models.CharField(max_length=10)
    platform = models.ForeignKey(StreamPlatformDetails1,on_delete=models.CASCADE,related_name='movieslist',null=True,blank=True)

    def __str__(self):
        return self.movie_name

