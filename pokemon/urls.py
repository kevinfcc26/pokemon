from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from pokemon.views import PokemonViewSet, TimeApiView

app_name = "pokemon"

router = DefaultRouter()
router.register(r"pokemon", PokemonViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r"^time/(?P<area>[^/]+)/(?P<location>[^/]+)(?:/(?P<region>[^/]+))?/?$", TimeApiView.as_view()),
]
