import os
import random
import time
import datetime

from pytz import timezone
from pathlib import Path

from django.core.files.base import ContentFile
from django.db import models

from django_app.settings import TIME_ZONE

BASE_DIR = Path(__file__).resolve().parent

IMAGE_PLACEHOLDER = ContentFile(open(BASE_DIR.joinpath('placeholder.png'), 'rb').read())
FILE_PLACEHOLDER = ContentFile(open(BASE_DIR.joinpath('placeholder.pdf'), 'rb').read())
VIDEO_PLACEHOLDER = ContentFile(open(BASE_DIR.joinpath('placeholder.mp4'), 'rb').read())
DOCX_PLACEHOLDER = ContentFile(open(BASE_DIR.joinpath('placeholder.docx'), 'rb').read())
XLSX_PLACEHOLDER = ContentFile(open(BASE_DIR.joinpath('placeholder.xlsx'), 'rb').read())


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop, only_date=False):
    parse_format = '%Y-%m-%d' if only_date else '%Y-%m-%d %H:%M'
    return datetime.datetime.strptime(
        str_time_prop(start, end, parse_format, prop), parse_format).replace(tzinfo=timezone(TIME_ZONE))


def get_random_models_ids(model: models):
    return {random.choice(model.objects.all()).id for _ in range(random.randint(1, model.objects.all().count()))}


def get_random_model(model: models):
    try:
        return random.choice(model.objects.all())
    except IndexError:
        return None


def add_many_to_model(model: models, to, model_to, ids):
    for Id in ids:
        getattr(model, to).add(model_to.objects.get(id=Id))


def true_or_false(true_value=None, false_value=None):
    res = bool(random.randint(0, 1))
    if true_value or false_value:
        res = true_value if true_value else false_value
    return res


def safe_prune(model: models):
    if bool(int(os.environ.get('USE_BOOTSTRAP_PRUNE_DB', False))):
        print(f'{model._meta.object_name} - Prune complete')
        model.objects.all().delete()
