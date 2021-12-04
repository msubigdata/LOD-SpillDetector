import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

import django

django.setup()

from api.v1.region.models import Region


def bootstrap_models(models: list):
    for model in models:
        model.bootstrap()
        print(f'{model.__name__} - Bootstrap complete')


if bool(int(os.environ.get('USE_BOOTSTRAP_DB', False))):  # Use bootstrap database (default False)
    bootstrap_models([
        Region
    ])
