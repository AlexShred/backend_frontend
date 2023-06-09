# Generated by Django 4.2.1 on 2023-05-07 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0002_onway_bol'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='load',
            name='delivery_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='load',
            name='pickup_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='PickupCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatch.state')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatch.state')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='load',
            name='delivery_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatch.deliverycity'),
        ),
        migrations.AlterField(
            model_name='load',
            name='pickup_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispatch.pickupcity'),
        ),
    ]
