from rest_framework.routers import DefaultRouter
from .views import ActorView, DirectorView, MovieDetailView, MovieView, RatingView, TestMovieView


router = DefaultRouter()
router.register('actor',ActorView)
router.register('movie',MovieView)
router.register('movie_detail',MovieDetailView)
router.register('director',DirectorView)
router.register('rating',RatingView)
router.register('test', TestMovieView, basename='test-movie')

urlpatterns = router.urls
