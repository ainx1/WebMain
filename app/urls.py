from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
# from PCShop import views
from PCShop.api import ComponentViewSet, CategoryViewSet, ManufacturerViewSet, OrderViewSet, OrderItemViewSet, PcBuildViewSet

router = DefaultRouter()
router.register(r'components', ComponentViewSet, basename='component')
router.register(r'categories', CategoryViewSet, basename='category')   
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='order-item')
router.register(r'pc-builds', PcBuildViewSet, basename='pc-build')

urlpatterns = [
    # path('', views.ShowComponentsView.as_view()),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
