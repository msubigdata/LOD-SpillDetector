from pathlib import Path
from typing import Union
import requests
import os

from django_app import settings
from django.core.files.base import ContentFile
from django_hashedfilenamestorage.storage import HashedFilenameFileSystemStorage

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")


def save_file_hashed(download_folder: str, file: bytes, extension: str, allowed_extensions="*") -> (str, str, str):
    file_name = f"temp.{extension}"
    file = ContentFile(file)
    storage = HashedFilenameFileSystemStorage(location=settings.MEDIA_ROOT)
    file_path = f"{storage.save(f'{download_folder}/{file_name}', file)}"
    if allowed_extensions != "*":
        if extension not in allowed_extensions:
            return None
    return file_path


def get_file_by_url(url: str) -> (bytes, str, bool):
    try:
        r = requests.get(url, stream=True)
    except Exception:
        return None, None, True
    if r.status_code != requests.codes['ok']:
        return None, None, True
    file_content = r.content
    file_extension = get_file_extension(url)
    return file_content, file_extension, False


def sanitize_extension(extension):
    return extension.replace("'", '').replace('"', '').replace('/', '')


def get_file_extension(file_path: Union[Path, str]) -> str:
    return sanitize_extension(file_path.split('.')[-1])


def create_dir(directory: [str, Path] = '.'):
    if directory.replace('.', ''):
        Path(f'{directory}').mkdir(exist_ok=True, parents=True)


def get_file_name(file_path: Union[Path, str]) -> str:
    return file_path.split('/')[-1].split('.')[0]
