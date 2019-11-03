from rest_framework.serializers import ModelSerializer

from .models import Houses

class HouseSerializer(ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'