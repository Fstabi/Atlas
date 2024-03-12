from rest_framework import serializers
from core.models import Level


class LevelSerializer(serializers.ModelSerializer):
    """Serializer for the Level model."""

    class Meta:
        model = Level
        fields = ['id', 'name', 'level_score']
        read_only_fields = ['id']