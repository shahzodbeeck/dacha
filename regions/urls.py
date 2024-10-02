from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProvinceViewSet, DistrictViewSet, PopularPlacesViewSet

router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'popular-places', PopularPlacesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
