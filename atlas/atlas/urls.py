from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('atlas.urls')),
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('user/', include('user.urls')),
    path('category/', include('category.urls')),
    path('level/', include('level.urls')),
    path('challenge/', include('challenge.urls')),
    path('score/', include('score.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]