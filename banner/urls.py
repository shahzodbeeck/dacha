from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannersViewSet

router = DefaultRouter()
router.register(r'banners', BannersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
