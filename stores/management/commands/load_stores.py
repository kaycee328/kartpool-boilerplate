import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from stores.models import Store  # Adjust the import based on your actual app name


class Command(BaseCommand):
    help = "Load OSM JSON data into the Store model"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the OSM JSON file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for element in data["elements"]:
            if element["type"] == "node" and "name" in element.get("tags", {}):
                location = Point(element["lon"], element["lat"])
                store, created = Store.objects.get_or_create(
                    id=str(element["id"]),
                    defaults={
                        "name": element["tags"]["name"],
                        "latitude": element["lat"],
                        "longitude": element["lon"],
                        "location": location,
                        "address": element["tags"].get("addr:street", ""),
                        "city": element["tags"].get("addr:city", ""),
                        "store_type": element["tags"].get("shop", None),
                        "phone": element["tags"].get("phone", None),
                        # You may need to adjust these fields depending on your OSM data
                    },
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created Store: {store.name}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Store already exists: {store.name}")
                    )

        self.stdout.write(self.style.SUCCESS("OSM data has been successfully loaded"))
