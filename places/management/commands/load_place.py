import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Load place from json'

    def add_arguments(self, parser):
        parser.add_argument('json', help='Json url')

    def handle(self, *args, **options):
        response = requests.get(options['json'])
        response.raise_for_status()
        response = response.json()

        place, created = Place.objects.get_or_create(
            title=response['title'],
            latitude=response['coordinates']['lat'],
            longitude=response['coordinates']['lng'],
            defaults={'short_description': response['description_short'],
                      'long_description': response['description_long']},
        )

        for pic_number, image_url in enumerate(response['imgs']):
            response = requests.get(image_url)
            response.raise_for_status()

            image = Image.objects.create(place=place)
            image.image.save(
                f'{place.title}_{pic_number}.jpg',
                ContentFile(response.content),
                save=True
            )
        if created:
            self.stdout.write('New place loaded.')
