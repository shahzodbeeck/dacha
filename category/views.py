from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, CategoryServices
from .serializers import CategorySerializer, CategoryServicesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryServicesViewSet(viewsets.ModelViewSet):
    queryset = CategoryServices.objects.all()
    serializer_class = CategoryServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
