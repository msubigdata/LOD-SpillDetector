from django.db import models

from bootstrap.utils import safe_prune


class Region(models.Model):
    name = models.CharField('Название', max_length=200)
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.name

    @staticmethod
    def bootstrap():
        items = [
            {'name': 'Москва', 'lat': 55.7522, 'long': 37.6156},
            {'name': 'Челябинск', 'lat': 55.1540200, 'long': 61.4291500},
            {'name': 'Хабаровск', 'lat': 48.4827100, 'long': 135.0837900},
            {'name': 'Казань', 'lat': 55.7887400, 'long': 49.1221400},
            {'name': 'Уфа', 'lat': 54.7430600, 'long': 55.9677900},
            {'name': 'Омск', 'lat': 54.9924400, 'long': 73.3685900},
            {'name': 'Киров', 'lat': 58.5966, 'long': 49.6601},
            {'name': 'Новосибирск', 'lat': 55.0415, 'long': 82.9346},
        ]

        safe_prune(Region)

        for item in items:
            Region.objects.create(
                name=item['name'],
                lat=item['lat'],
                long=item['long'],
            )


