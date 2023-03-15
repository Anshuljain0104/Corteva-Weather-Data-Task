from rest_framework import serializers
from .models import WeatherData, WeatherStats


class WeatherDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ["station_id", "date", "max_temperature", "min_temperature", "precipitation"]


class WeatherStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        fields = ["station_id", "year", "avg_max_temperature", "avg_min_temperature", "total_precipitation"]
