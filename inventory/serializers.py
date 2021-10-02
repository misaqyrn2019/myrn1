from rest_framework import serializers
from .models import Commodity
from drf_dynamic_fields import DynamicFieldsMixin

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        exclude = ["Id"]