from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet

app_name = "pokemon"

router = DefaultRouter()
router.register(r"pokemons", PokemonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
