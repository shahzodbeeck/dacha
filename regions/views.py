from rest_framework import viewsets
from .models import Province, District, PopularPlaces
from .serializers import ProvinceSerializer, DistrictSerializer, PopularPlacesSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class PopularPlacesViewSet(viewsets.ModelViewSet):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesSerializer
