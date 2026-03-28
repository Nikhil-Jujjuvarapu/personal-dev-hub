from django.shortcuts import render
from users.models import StreamPlatformDetails1, MoviesDetails1
from rest_framework import generics
from rest_framework.response import Response
from .serializers import StreamPlatformSerializer, WatchListSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

class StreamPlatformView(generics.ListCreateAPIView):
    queryset = StreamPlatformDetails1.objects.prefetch_related('movieslist')
    serializer_class = StreamPlatformSerializer

class StreamPlatformRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatformDetails1.objects.all()
    serializer_class = StreamPlatformSerializer

class WatchListView(generics.ListCreateAPIView):
    queryset = MoviesDetails1.objects.all()
    serializer_class = WatchListSerializer
 
# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MoveListSerializer

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method =='GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie id not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MoveListSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MoveListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'Deleted the following id: ',pk},status=status.HTTP_204_NO_CONTENT)