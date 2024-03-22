from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router object
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'', views.BasicChallengeViewSet)
router.register(r'area-challenge', views.AreaChallengeViewSet)
router.register(r'coordinate-challenge', views.CoordinateChallengeViewSet)


# Define the app name
app_name = 'challenge'

# Define the urlpatterns
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]
