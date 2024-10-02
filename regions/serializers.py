from rest_framework import serializers

from .models import Province, District, PopularPlaces


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'translated_name']


class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'translated_name', 'province']


class PopularPlacesSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = PopularPlaces
        fields = ['id', 'name', 'translated_name', 'district']
