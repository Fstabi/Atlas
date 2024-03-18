from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router object
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'', views.ChallengeViewSet)
router.register(r'simple-challenge', views.ChallengeViewSet)
router.register(r'area-challenge', views.ChallengeViewSet)
router.register(r'coordinate-challenge', views.ChallengeViewSet)


# Define the app name
app_name = 'challenge'

# Define the urlpatterns
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]
