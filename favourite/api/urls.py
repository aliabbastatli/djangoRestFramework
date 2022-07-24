from django.urls import path

from favourite.api.views import (
    FavoriteListCreateAPIView, FavoriteAPIView,
)
app_name = "favourite"
urlpatterns = [
    path('list-create', FavoriteListCreateAPIView.as_view(), name='list-create'),
    path('update-delete/<pk>', FavoriteAPIView.as_view(), name='update-delete'),
]
