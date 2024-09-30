from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryServicesViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'category_services', CategoryServicesViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
