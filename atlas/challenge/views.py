from rest_framework import viewsets
from core.models import BasicChallenge, AreaChallenge, CoordinateChallenge
from .serializers import ChallengesSerializer
from .permissions import IsAdminUserOrReadOnly, IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BasicChallengeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing simple challenges.
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

class AreaChallengeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing area challenges.
    """
    queryset = AreaChallenge.objects.all()
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

class CoordinateChallengeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing coordinate challenges.
    """
    queryset = CoordinateChallenge.objects.all()
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
