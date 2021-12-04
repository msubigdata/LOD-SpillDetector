from django.urls import path

from .views import InspectCreateView

urlpatterns = [
    path('', InspectCreateView.as_view()),
]
