from rest_framework import serializers
from .models import StreamPlatformDetails1, MoviesDetails1



class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MoviesDetails1
        fields = "__all__"

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    movieslist = WatchListSerializer(many=True, read_only=True)
    # movieslist = WatchListSerializer.objects.prefetch_related('movieslist')
    url = serializers.HyperlinkedIdentityField(view_name='streamplatform-detail')
    class Meta:
        model = StreamPlatformDetails1
        fields = "__all__"
    