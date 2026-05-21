from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Mountain
from .serializers import MountainSerializer
from .filters import MountainFilter  # Import your new filter layer

class MountainViewSet(viewsets.ModelViewSet):
    queryset = Mountain.objects.all().order_by('-elevation_ft')
    serializer_class = MountainSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    filterset_class = MountainFilter
    
    search_fields = ['name']
