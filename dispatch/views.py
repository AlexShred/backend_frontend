from rest_framework import generics
from .models import Driver, Truck, Load, Onway
from .serializers import DriverSerializer, TruckSerializer, LoadSerializer, OnwaySerializer


class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class LoadListCreateView(generics.ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer


class LoadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
class TruckListCreateView(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class OnwayListCreateView(generics.ListCreateAPIView):
    queryset = Onway.objects.all()
    serializer_class = OnwaySerializer


class OnwayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Onway.objects.all()
    serializer_class = OnwaySerializer