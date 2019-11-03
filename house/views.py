from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Houses
from .serializers import HouseSerializer


class HouseViewSet(ModelViewSet):
    queryset = Houses.objects.all()
    serializer_class = HouseSerializer