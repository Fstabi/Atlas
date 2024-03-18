from rest_framework import serializers
from core.models import BasicChallenge, AreaChallenge, CoordinateChallenge, SimpleChallenge

class ChallengesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Challenges model.
    """
    class Meta:
        model = BasicChallenge
        fields = ['id', 'name', 'category_id', 'level_id', 'score_id']
        read_only_fields = ['id', 'category_id', 'level_id', 'score_id']  # Fields that won't be returned to the user

class SimpleChallengeSerializer(serializers.ModelSerializer):
    """
    Serializer for the SimpleChallenge model.
    """
    class Meta:
        model = SimpleChallenge
        fields = ['id', 'name', 'description', 'category_id', 'level_id', 'score_id', 'photo_link']
        read_only_fields = ['id', 'category_id', 'level_id', 'score_id', 'photo_link']   

class AreaChallengeSerializer(serializers.ModelSerializer):
    """
    Serializer for the AreaChallenge model.
    """
    class Meta:
        model = AreaChallenge
        fields = ['id', 'name', 'category_id', 'level_id', 'score_id', 'photo_link', 'area']
        read_only_fields = ['id', 'category_id', 'level_id', 'score_id', 'photo_link', 'area']   

class CoordinateChallengeSerializer(serializers.ModelSerializer):
    """
    Serializer for the CoordinateChallenge model.
    """
    class Meta:
        model = CoordinateChallenge
        fields = ['id', 'name', 'category_id', 'level_id', 'score_id','photo_link', 'lat', 'long']
        read_only_fields = ['id', 'category_id', 'level_id', 'score_id', 'photo_link', 'lat', 'long']  