from rest_framework import serializers
from PCShop.models import Component, Category, Manufacturer, Order, OrderItem, PcBuild


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country']


class ComponentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Component
        fields = ['id', 'name', 'category', 'manufacturer', 'price', 'stock', 'description', 'image']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_phone', 'status', 'date', 'time']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ComponentSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']


class PcBuildSerializer(serializers.ModelSerializer):
    product = ComponentSerializer(many=True, read_only=True)

    class Meta:
        model = PcBuild
        fields = ['id', 'name', 'product', 'image']