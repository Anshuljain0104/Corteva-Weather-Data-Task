from django.db import models


class WeatherData(models.Model):
    date = models.CharField(max_length=8)
    max_temperature = models.IntegerField()
    min_temperature = models.IntegerField()
    precipitation = models.IntegerField()
    station_id = models.CharField(max_length=11)

    class Meta:
        unique_together = ("station_id", "date")


class WeatherStats(models.Model):

    station_id = models.CharField(max_length=11)
    year = models.CharField(max_length=4)
    avg_max_temperature = models.FloatField()
    avg_min_temperature = models.FloatField()
    total_precipitation = models.IntegerField()

    class Meta:
        unique_together = ("station_id", "year")
