from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from favourite.api.serializers import FavoriteListCreateAPISerializer, FavoriteAPISerializer
from favourite.models import Favourite


class FavoriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavoriteListCreateAPISerializer
    pagination_class = FavouritePagination

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavoriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
