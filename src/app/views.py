from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import WeatherStats, WeatherData
from .serializers import WeatherDataSerializers, WeatherStatsSerializers


class WeatherDataView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["station_id", "date"]


class WeatherStatsView(generics.ListAPIView):
    queryset = WeatherStats.objects.all()
    serializer_class = WeatherStatsSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["station_id", "year"]
