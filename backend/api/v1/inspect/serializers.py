from rest_framework.serializers import ModelSerializer

from api.v1.inspect.models import Inspect


class InspectSerializer(ModelSerializer):
    class Meta:
        model = Inspect
        fields = '__all__'

