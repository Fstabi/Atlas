from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScoreViewSet

# Create a router and register the ScoreViewSet with it
router = DefaultRouter()
router.register(r'', ScoreViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
