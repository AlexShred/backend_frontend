from rest_framework import serializers
from .models import Truck, State, City, PickupCity, DeliveryCity, Driver, Load, Onway

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class PickupCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupCity
        fields = '__all__'

class DeliveryCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCity
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    truck = TruckSerializer()

    class Meta:
        model = Driver
        fields = '__all__'

class LoadSerializer(serializers.ModelSerializer):
    pickup_city = PickupCitySerializer()
    delivery_city = DeliveryCitySerializer()
    drivers = DriverSerializer(many=True)

    class Meta:
        model = Load
        fields = '__all__'

class OnwaySerializer(serializers.ModelSerializer):
    load = LoadSerializer()
    driver = DriverSerializer()

    class Meta:
        model = Onway
        fields = '__all__'