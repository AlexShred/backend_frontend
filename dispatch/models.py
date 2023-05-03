from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


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
    pickup_city = models.CharField(max_length=50, choices=(("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")))
    delivery_city = models.CharField(max_length=50, choices=(("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")))
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