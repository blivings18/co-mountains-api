from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Mountain

class MountainAPITests(APITestCase):

    def setUp(self):
        """
        Create sample data in a temporary test database before each test runs.
        """
        self.elbert = Mountain.objects.create(
            name="Mount Elbert",
            range_name="Sawatch Range",
            elevation_ft=14440,
            is_fourteener=True,
            prominence_ft=9093,
            isolation_mi=67.0,
            latitude=39.1178,
            longitude=-106.4454,
            standard_route="Northeast Ridge",
            difficulty="Class 1"
        )
        self.massive = Mountain.objects.create(
            name="Mount Massive",
            range_name="Sawatch Range",
            elevation_ft=14421,
            is_fourteener=True,
            prominence_ft=1961,
            isolation_mi=5.0,
            latitude=39.1875,
            longitude=-106.4757,
            standard_route="East Slopes",
            difficulty="Class 2"
        )
        self.foothill = Mountain.objects.create(
            name="Mount Morrison",
            range_name="Front Range",
            elevation_ft=7881,
            is_fourteener=False,
            prominence_ft=600,
            isolation_mi=2.5,
            latitude=39.6521,
            longitude=-105.2031,
            standard_route="South Ridge",
            difficulty="Class 2"
        )
        # API URL helper
        self.url = reverse('mountain-list')

    def test_override_default_elevation(self):
        """
        Ensure passing an explicit min_elevation overrides the default threshold
        and includes lower peaks.
        """
        response = self.client.get(self.url, {'min_elevation': 0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Should return all 3 mountains now
        self.assertEqual(len(response.data), 3)

    def test_filter_by_range(self):
        """
        Ensure range_name exact filtering works properly.
        """
        response = self.client.get(self.url, {'range_name': 'Sawatch Range'})
        self.assertEqual(len(response.data), 2)
        
        # Ensure it didn't pull the Front Range peak
        for mountain in response.data:
            self.assertEqual(mountain['range_name'], 'Sawatch Range')

    def test_fuzzy_search(self):
        """
        Ensure fuzzy text search matches partial peak names.
        """
        response = self.client.get(self.url, {'search': 'Elb'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Mount Elbert")
