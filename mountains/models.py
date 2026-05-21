from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    range_name = models.CharField(max_length=100)
    elevation_ft = models.IntegerField()
    is_fourteener = models.BooleanField(default=False)
    prominence_ft = models.IntegerField()
    isolation_mi = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    standard_route = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.elevation_ft} ft)"
