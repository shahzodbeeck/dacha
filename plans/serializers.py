from rest_framework import serializers

from .models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'id',
            'name', 'name_uz', 'name_en', 'name_ru',
            "description", 'description_uz', 'description_en', 'description_ru',
            'price',
            'duration'
        ]
