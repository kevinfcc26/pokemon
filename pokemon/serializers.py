from rest_framework import serializers

from core.models.pokemon import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """Serializer for the users objects"""

    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Pokemon
        fields = ("id", "name", "type", "abilities", "description", "is_public", "user_email")
        read_only_fields = ("id", "user")
