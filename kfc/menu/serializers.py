from .models import Menu
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
