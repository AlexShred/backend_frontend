from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
import us


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey('State', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}, {self.state.state_code}"


class PickupCity(City):
    def __str__(self):
        return f"{self.name}, {self.state.state_code} (Pickup City)"


class DeliveryCity(City):
    def __str__(self):
        return f"{self.name}, {self.state.state_code} (Delivery City)"


class State(models.Model):
    state_code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Truck(models.Model):
    name = models.CharField(max_length=50)
    date_of_manufacture = models.DateField()

    def clean(self):
        if self.date_of_manufacture > date.today():
            raise ValidationError('Date of manufacture can not be in the future')

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=50)
    readiness = models.CharField(max_length=50, choices=(
        ('ready', 'Ready'),
        ('not_ready', 'Not ready'),
    ))
    truck = models.OneToOneField(Truck, on_delete=models.CASCADE)
    citizenship = models.CharField(max_length=50, choices=(
        ('have', 'Have'),
        ('havent', 'Haven\'t'),
    ))
    cards = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Load(models.Model):
    cargo = models.CharField(max_length=50)
    pickup_date = models.DateField(default=date.today)
    delivery_date = models.DateField()
    pickup_city = models.ForeignKey(PickupCity, on_delete=models.CASCADE)
    delivery_city = models.ForeignKey(DeliveryCity, on_delete=models.CASCADE)
    trip = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    contact_number_ex = models.CharField(max_length=50)
    weight = models.CharField(max_length=50, null=True, blank=True)
    length = models.CharField(max_length=50, null=True, blank=True)
    rate = models.CharField(max_length=50)
    drivers = models.ManyToManyField(Driver, related_name="loads", through="Onway")

    def clean(self):
        if self.delivery_date < self.pickup_date:
            raise ValidationError('Delivery date can not be earlier than pickup date')

    def __str__(self):
        return self.cargo


class Onway(models.Model):
    bol = models.ImageField(null=True)
    last_location = models.CharField(max_length=50)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_location