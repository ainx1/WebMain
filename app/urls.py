from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from PCShop.api import (
    ComponentViewSet, 
    CategoryViewSet,
    ManufacturerViewSet, 
    OrderViewSet, 
    OrderItemViewSet, 
    PcBuildViewSet,
    ProfileViewSet
)

router = DefaultRouter()
router.register('components', ComponentViewSet, basename='component')
router.register('categories', CategoryViewSet, basename='category')   
router.register('manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register('orders', OrderViewSet, basename='order')
router.register('order-items', OrderItemViewSet, basename='order-item')
router.register('pc-builds', PcBuildViewSet, basename='pc-build')
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

