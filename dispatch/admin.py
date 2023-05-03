from django.contrib import admin

from .models import Truck, Driver, Load, Onway

admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Load)
admin.site.register(Onway)

