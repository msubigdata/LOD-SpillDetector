from django.db import models

from bootstrap.utils import safe_prune


class Inspect(models.Model):
    bbox = models.JSONField('Координаты зоны', default=[])

    def __str__(self):
        return self.bbox


