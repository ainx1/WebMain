from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response


from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate



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


class ProfileViewSet(GenericViewSet):
    queryset = User.objects.all()

    @action(detail=False, url_path='me', methods=['GET'])
    def get_me(self, request, *args, **kwargs):
        data = {
            'is_authenticated': self.request.user.is_authenticated,

        }
        if self.request.user.is_authenticated:
            data.update({
                'username': self.request.user.username,
                'id': self.request.user.id,
                'role': self.request.user.profile.role,
                'phone': self.request.user.profile.phone,
                'address': self.request.user.profile.address,
            })

        return Response(data=data)

    @action(detail=False, url_path="logout", methods=["POST"])
    def logout(self, *args, **kwargs):
        django_logout(self.request)

        return Response()
    
    @action(detail=False, url_path="login", methods=['POST'])
    def login(self, *args, **kwargs):
        username = self.request.data['username']
        password = self.request.data['password']

        success = False
        status_code = 403

        user = authenticate(username=username, password=password)
        if user:
            success = True
            status_code = 200
            django_login(self.request, user)

        return Response({
            'success': success
        }, status=status_code)