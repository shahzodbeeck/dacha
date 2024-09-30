from rest_framework import serializers
from .models import Banners


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ['id', 'name', 'link', 'price', 'image']
