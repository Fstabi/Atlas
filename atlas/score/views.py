from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from core.models import Score
from .serializers import ScoreSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing scores.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

