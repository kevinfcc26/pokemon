from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exepctions import ProviderException
from core.models.pokemon import Pokemon
from pokemon.adapters.word_time import WorldTimeAdapter
from pokemon.transport.word_time import WorldTimeAPI
from user.authentication import BearerAuthentication

from .serializers import PokemonSerializer, WorldTimeSerializer


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


class TimeApiView(APIView):
    def get(self, request, area, location, region=None):
        try:
            world_time_api = WorldTimeAPI()
            data = world_time_api.get_time(area, location, region)

            adapted_data = WorldTimeAdapter.adapt(data)

            serializer = WorldTimeSerializer(adapted_data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProviderException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
