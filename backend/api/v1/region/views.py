from rest_framework.generics import ListAPIView

from api.v1.region.models import Region
from api.v1.region.serializers import RegionSerializer


class RegionListView(ListAPIView):
    """
    Регионы

    Получить список регионов для карты
    """

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
