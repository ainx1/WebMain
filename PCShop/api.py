from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from PCShop.models import (
    Component,
    Category, 
    Manufacturer, 
    Order, OrderItem,
    PcBuild
)

from PCShop.serializers import (
    ComponentSerializer,
    CategorySerializer,
    ManufacturerSerializer,
    OrderSerializer,
    OrderItemSerializer,
    PcBuildSerializer,
)


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ManufacturerViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ComponentViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class PcBuildViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = PcBuild.objects.all()
    serializer_class = PcBuildSerializer