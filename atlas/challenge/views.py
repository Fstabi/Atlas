from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from core.models import BasicChallenge
from .serializers import ChallengesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsAdminUserOrReadOnly


class ChallengeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing challenges.
    """
    queryset = BasicChallenge.objects.all()
    serializer_class = ChallengesSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        """
        Override the method to include custom permissions for specific actions.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Override the method to set additional fields during object creation.
        """
        serializer.save(created_by=self.request.user)

