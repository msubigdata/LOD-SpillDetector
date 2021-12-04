from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from django_app import settings

urlpatterns = [
    path('api/grappelli/', include('grappelli.urls')),
    path('api/admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
    url(r'^api/_nested_admin/', include('nested_admin.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
