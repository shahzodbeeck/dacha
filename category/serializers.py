from rest_framework import serializers
from .models import Category, CategoryServices


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'name_en', 'name_ru']


class CategoryServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryServices
        fields = ['id', 'name', 'image']
