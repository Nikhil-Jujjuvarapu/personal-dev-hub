from .serializers import ActorSerializer, MovieDetailSerializer, MovieSerializer, RatingSerializer, DirectorSerializer, TestMovieSerializer
from .models import Actor, Movie, MovieDetail, Rating, Director
from rest_framework import viewsets


class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = (
            Movie.objects.select_related("director", "details")
            .prefetch_related("actors", "ratings")
        )
        director_name = self.request.query_params.get("director")
        if director_name:
            queryset = queryset.filter(director__name__iexact=director_name)
        return queryset


class MovieDetailView(viewsets.ModelViewSet):
    queryset = MovieDetail.objects.select_related("movie")
    serializer_class = MovieDetailSerializer


class DirectorView(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.select_related("movie", "user")
    serializer_class = RatingSerializer


class TestMovieView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    # queryset = Movie.objects.filter(id=1).select_related("director", "details").prefetch_related("actors", "ratings")
    serializer_class = TestMovieSerializer

