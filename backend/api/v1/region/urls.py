from django.urls import path

from .views import RegionListView

urlpatterns = [
    path('', RegionListView.as_view()),
]
