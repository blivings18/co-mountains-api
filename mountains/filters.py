from django_filters import rest_framework as filters
from .models import Mountain

class MountainFilter(filters.FilterSet):
    # Custom Elevation Filters (Greater than / Less than)
    min_elevation = filters.NumberFilter(field_name="elevation_ft", lookup_expr='gte', label="Minimum Elevation (ft)")
    max_elevation = filters.NumberFilter(field_name="elevation_ft", lookup_expr='lte', label="Maximum Elevation (ft)")

    # Dropdown Filters generated dynamically from database content
    range_name = filters.ChoiceFilter(choices=[], label="Mountain Range")
    difficulty = filters.ChoiceFilter(choices=[], label="Difficulty Class")

    class Meta:
        model = Mountain
        fields = ['is_fourteener', 'range_name', 'difficulty', 'min_elevation', 'max_elevation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Pull unique ranges and difficulties currently in the database to build the dropdown options
        try:
            ranges = Mountain.objects.values_list('range_name', flat=True).distinct().order_by('range_name')
            self.filters['range_name'].extra['choices'] = [(r, r) for r in ranges if r]
            
            difficulties = Mountain.objects.values_list('difficulty', flat=True).distinct().order_by('difficulty')
            self.filters['difficulty'].extra['choices'] = [(d, d) for d in difficulties if d]
        except Exception:
            # Prevents initial migration/scaffolding commands from crashing if database isn't fully built yet
            pass
