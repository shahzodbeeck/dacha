from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Banners
from .serializers import BannersSerializer


class BannersViewSet(viewsets.ModelViewSet):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
