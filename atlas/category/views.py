from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from core.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """View for managing category."""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]