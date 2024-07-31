from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from menu.models import Menu
from menu.serializers import MenuSerializers


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [AllowAny]
