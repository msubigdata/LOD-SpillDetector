import functools
from operator import attrgetter

from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class AdminPhotoPreviewMixin:
    def photo_preview(self, obj):
        return get_photo_preview(obj.photo)

    photo_preview.short_description = 'Изображение'
    photo_preview.allow_tags = True


def get_photo_preview(file):
    return format_html('<img src="{}" width="{}" height="{}" style="object-fit: contain;">'.format(file.url, 150, 150))


def get_objects_change_links(obj, set_name):
    set_objects = getattr(obj, set_name).all()
    links = []
    for set_object in set_objects:
        links.append(get_change_link_by_object(set_object))
    return mark_safe(", ".join(links)) if links else None


def get_object_change_link(obj, fk_name):
    if '.' in fk_name:
        fk_obj = attrgetter(fk_name)(obj)
    else:
        fk_obj = getattr(obj, fk_name)
    if not fk_obj:
        return None
    link = get_change_link_by_object(fk_obj)
    return mark_safe(link) if link else None


def get_change_link_by_object(obj):
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.app_label), args=(obj.id,))
    link = f'<a href="{url}">{obj.name}</a>'
    return link
