from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Categorie model."""

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']