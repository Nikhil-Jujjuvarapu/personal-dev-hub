from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import MoviesDetails1, StreamPlatformDetails1


class StreamPlatformApiTests(APITestCase):
    def setUp(self):
        self.platform = StreamPlatformDetails1.objects.create(
            name="Netflix",
            description="Streaming app",
        )
        self.movie = MoviesDetails1.objects.create(
            movie_name="Avatar",
            release_year=2009,
            language="English",
            platform=self.platform,
        )

    def test_get_stream_platform_list(self):
        url = reverse("watch-list-platform")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Netflix")
        self.assertEqual(response.data[0]["movieslist"][0]["movie_name"], "Avatar")

    def test_create_movie_details(self):
        url = reverse("watchlist")
        payload = {
            "movie_name": "Joker",
            "release_year": 2019,
            "language": "English",
            "platform": self.platform.id,
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MoviesDetails1.objects.count(), 2)
        self.assertEqual(MoviesDetails1.objects.get(movie_name="Joker").release_year, 2019)
