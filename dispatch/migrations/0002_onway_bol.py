# Generated by Django 4.2.1 on 2023-05-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onway',
            name='bol',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]