from django.urls import path
from .views import *

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # YOUR PATTERNS
    path(r"weather/", WeatherDataView.as_view(), name="weather_data"),
    path(r"weather/stats/", WeatherStatsView.as_view(), name="weather_stats"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
