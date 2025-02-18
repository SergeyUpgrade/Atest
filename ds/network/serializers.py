from rest_framework import serializers
from .models import Product, NetworkNode

class ProductSerializer(serializers.ModelSerializer):
    """
    Настройка, чтобы видеть все поля для модели Product
    """
    class Meta:
        model = Product
        fields = '__all__'

class NetworkNodeSerializer(serializers.ModelSerializer):
    """
    Настройка, чтобы видеть все поля для модели NetworkNode, где можно выбрать один продукт/продукты из имеющихся
    """
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)
