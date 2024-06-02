from rest_framework import permissions, viewsets

from core.models.pokemon import Pokemon
from user.authentication import BearerAuthentication

from .serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = (BearerAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pokemon.objects.filter(user=self.request.user) | Pokemon.objects.filter(is_public=True)
        return Pokemon.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
