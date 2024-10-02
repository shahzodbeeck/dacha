from rest_framework import serializers

from .models import Province, District, PopularPlaces


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'name_en', 'name_ru','name_uz']


class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)

    class Meta:
        model = District
        fields = ['id', 'name', 'name_en', 'name_ru','name_uz', 'province']


class PopularPlacesSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = PopularPlaces
        fields = ['id', 'name', 'name_en', 'name_ru','name_uz', 'district']
