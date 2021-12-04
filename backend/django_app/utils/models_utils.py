from PIL import Image

from django.apps import apps
from django.db import models

from django_app.utils.text_utils import get_proxy_item_name


def get_complete_name(model_obj: models, text: str) -> str:
    return get_proxy_item_name(text, get_app_verbose_name(model_obj))


def get_from_model_meta(model_obj: models, attribute: str):
    return getattr(model_obj._meta, attribute)


def get_app_label_meta(model_obj: models, attribute: str = 'app_label') -> str:
    return get_from_model_meta(model_obj, attribute)


def get_app_verbose_name(model_obj: models) -> str:
    return apps.get_app_config(model_obj._meta.app_label).verbose_name


def get_verbose_name_meta(model_obj: models, attribute: str = 'verbose_name') -> str:
    return get_from_model_meta(model_obj, attribute)


def get_verbose_name_plural_meta(model_obj: models, attribute: str = 'verbose_name_plural') -> str:
    return get_from_model_meta(model_obj, attribute)


def get_verbose_names_meta(model_obj: models) -> [str, str]:
    return get_verbose_name_meta(model_obj), get_complete_name(model_obj, get_verbose_name_plural_meta(model_obj))


def get_ordering_field() -> models.PositiveIntegerField:
    return models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)


def fix_ordering(model_obj: models):
    for i, model in enumerate(model_obj.objects.all()):
        model.ordering = i
        model.save()
