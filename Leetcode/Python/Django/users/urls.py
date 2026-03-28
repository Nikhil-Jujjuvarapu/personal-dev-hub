from django.urls import path, include
from users.views import StreamPlatformView,WatchListView,StreamPlatformRUDView

urlpatterns = [
    path('streampaltform/', StreamPlatformView.as_view(), name='watch-list-platform'),
    path('streampaltform/<int:pk>', StreamPlatformRUDView.as_view(), name='streamplatform-detail'),
    path('moviedetails/',WatchListView.as_view(),name='watchlist'),
]
