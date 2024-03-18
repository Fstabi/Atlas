from rest_framework import serializers
from core.models import Score

class ScoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Score model.
    """
    class Meta:
        model = Score
        fields = ['id', 'user', 'challenge', 'score']
        read_only_fields = ['user', 'challenge', 'score']

