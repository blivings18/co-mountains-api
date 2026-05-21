from rest_framework import viewsets
from .models import Mountain
from .serializers import MountainSerializer

class MountainViewSet(viewsets.ModelViewSet):
    queryset = Mountain.objects.all().order_by('-elevation_ft') # Highest peaks first!
    serializer_class = MountainSerializer
