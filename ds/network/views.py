from rest_framework import viewsets
from .models import NetworkNode
from .serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    Создаем CRUD для звеньев сети электроники с возможностью фильтрации по стране
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filterset_fields = ['country']
