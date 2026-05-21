from rest_framework import serializers
from .models import Mountain

class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = [
            'id', 'name', 'range_name', 'elevation_ft', 'is_fourteener', 
            'prominence_ft', 'isolation_mi', 'latitude', 'longitude', 
            'standard_route', 'difficulty'
        ]
