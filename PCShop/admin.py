from django.contrib import admin

from PCShop.models import Profile, Category, Manufacturer, Component, Order, OrderItem, PcBuild

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "manufacturer", "price", "stock", "description", "image")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "customer_phone", "status", "date", "time")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")

@admin.register(PcBuild)
class PcBuildAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")
