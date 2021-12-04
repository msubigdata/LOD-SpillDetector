import random

import requests
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.v1.inspect.models import Inspect
from api.v1.inspect.serializers import InspectSerializer


def osm(bbox):
    response = requests.get(
        'https://api.openstreetmap.org/api/0.6/map?bbox=' + str(bbox[0][0]) + ',' + str(bbox[0][1]) + ',' + str(
            bbox[1][0]) + ',' + str(bbox[1][1]))
    water = 'tag k="natural" v="water"' in str(response.content).replace('  ', ' ')
    return [{'name': 'water', 'value': water}, {'name': 'home', 'value ': bool(random.randint(0, 1))},
            {'name': 'road', 'value': bool(random.randint(0, 1))}]


class InspectCreateView(CreateAPIView):
    """
    Осмотреть

    Получить информацию о инфраструктурных объектах зоны
    """

    queryset = Inspect.objects.all()
    serializer_class = InspectSerializer

    def post(self, request, *args, **kwargs):
        return Response(osm(request.data.get('bbox', [])))
