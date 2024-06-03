from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from pokemon.models.pokemon import Pokemon
from pokemon_2.serializers import PokemonSerializer

POKEMON_URL = reverse("pokemon:pokemon-list")


def detail_url(pokemon_id):
    """Return pokemon detail URL"""
    return reverse("pokemon:pokemon-detail", args=[pokemon_id])


def sample_pokemon(user, **params):
    """Create and return a sample pokemon"""
    defaults = {
        "name": "sample pokemon",
        "type": "sample type",
        "abilities": "sample abilities",
        "description": "it is a sample",
        "is_public": False,
    }
    defaults.update(params)

    return Pokemon.objects.create(user=user, **defaults)


class PublicPokemonApiTests(TestCase):
    """Tests unauthenticated pokemon API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authentication is required"""
        res = self.client.post(POKEMON_URL, {})

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePokemonApiTests(TestCase):
    """Test unauthenticated pokemon API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test@gmail.com", "testpass")
        self.client.force_authenticate(self.user)

    def test_retrieve_pokemon(self):
        """Test retrieve a list of Pokemon"""
        sample_pokemon(user=self.user)
        sample_pokemon(user=self.user)

        res = self.client.get(POKEMON_URL)

        pokemon = Pokemon.objects.all().order_by("id")
        serializer = PokemonSerializer(pokemon, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_pokemon_detail(self):
        """Test viewing a pokemon detail"""
        pokemon = sample_pokemon(user=self.user)

        url = detail_url(pokemon.id)
        res = self.client.get(url)

        serializer = PokemonSerializer(pokemon)
        self.assertEqual(res.data, serializer.data)

    def test_create_basic_pokemon(self):
        """Test creating pokemon"""
        payload = {
            "name": "sample pokemon",
            "type": "sample type",
            "abilities": "sample abilities",
            "description": "it is a sample",
            "is_public": False,
        }
        res = self.client.post(POKEMON_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        pokemon = Pokemon.objects.get(id=res.data["id"])
        for attr, val in payload.items():
            self.assertEqual(val, getattr(pokemon, attr))

    def test_partial_update_pokemon(self):
        """Test updating a pokemon with patch"""
        pokemon = sample_pokemon(user=self.user)

        payload = {"name": "test2"}
        url = detail_url(pokemon.id)
        self.client.patch(url, payload)

        pokemon.refresh_from_db()
        self.assertEqual(pokemon.name, payload["name"])

    def test_full_update_pokemon(self):
        """Test updating a pokemon with put"""
        pokemon = sample_pokemon(user=self.user)
        payload = {
            "name": "sample2 pokemon",
            "type": "sample2 type",
            "abilities": "sample2 abilities",
            "description": "it is a sample",
            "is_public": False,
        }
        url = detail_url(pokemon.id)
        self.client.put(url, payload)

        pokemon.refresh_from_db()
        self.assertEqual(pokemon.name, payload["name"])
        self.assertEqual(pokemon.type, payload["type"])
        self.assertEqual(pokemon.abilities, payload["abilities"])
        self.assertEqual(pokemon.description, payload["description"])
