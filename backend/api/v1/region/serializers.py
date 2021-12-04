from rest_framework.serializers import ModelSerializer

from api.v1.region.models import Region


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

