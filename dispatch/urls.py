from django.urls import path
from .views import (
    TruckListCreateView,
    TruckRetrieveUpdateDestroyView,
    DriverListCreateView,
    DriverRetrieveUpdateDestroyView,
    LoadListCreateView,
    LoadRetrieveUpdateDestroyView,
    OnwayListCreateView,
    OnwayRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('trucks/', TruckListCreateView.as_view(), name='truck_list'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyView.as_view(), name='truck_detail'),
    path('drivers/', DriverListCreateView.as_view(), name='driver_list'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyView.as_view(), name='driver_detail'),
    path('loads/', LoadListCreateView.as_view(), name='load_list'),
    path('loads/<int:pk>/', LoadRetrieveUpdateDestroyView.as_view(), name='load_detail'),
    path('onway/', OnwayListCreateView.as_view(), name='onway_list'),
    path('onway/<int:pk>/', OnwayRetrieveUpdateDestroyView.as_view(), name='onway_detail'),
]