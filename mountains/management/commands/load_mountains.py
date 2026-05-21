import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from mountains.models import Mountain

class Command(BaseCommand):
    help = 'Imports Colorado mountains from a custom CSV'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data', 'mountains.csv')
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"CSV missing at {file_path}"))
            return

        with open(file_path, mode='r', encoding='cp1252') as file:
            reader = csv.DictReader(file)
            count = 0
            
            for row in reader:
                # Safely convert 'Y'/'N' string to a real Python Boolean
                fourteener_bool = row['fourteener'].strip().upper() == 'Y'

                Mountain.objects.get_or_create(
                    name=row['Mountain Peak'],
                    range_name=row['Mountain Range'],
                    elevation_ft=int(row['Elevation_ft']),
                    is_fourteener=fourteener_bool,
                    prominence_ft=int(row['Prominence_ft']),
                    isolation_mi=float(row['Isolation_mi']),
                    latitude=float(row['Lat']),
                    longitude=float(row['Long']),
                    standard_route=row['Standard Route'],
                    difficulty=row['Difficulty']
                )
                count += 1
                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} peaks!'))
