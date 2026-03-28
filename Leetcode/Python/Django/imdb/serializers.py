from rest_framework import serializers
from .models import Actor,  MovieDetail, Director, Rating, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieDetailInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetail
        fields = ["duration_minutes", "budget"]


class MovieRatingInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["rating", "description"]


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    director = serializers.CharField(source="director.name", read_only=True)
    details = MovieDetailInlineSerializer(read_only=True)
    ratings = MovieRatingInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["title", "actors", "director", "details","ratings"]


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    movie = serializers.SlugRelatedField(
        many=False,
        slug_field="title",
        queryset=Movie.objects.all(),
    )

    class Meta:
        model = Rating
        fields = ["user", "movie", "rating", "description"]

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
class MovieDetailSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(
        many=False,
        slug_field = "title",
        queryset = Movie.objects.all(),
        
    )

    class Meta:
        model = MovieDetail
        fields = ['movie','duration_minutes','budget']
    
class TestMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
