from rest_framework import serializers

from .models import Truck, Driver, Load, Onway


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = "__all__"


class OnwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Onway
        fields = "__all__"
