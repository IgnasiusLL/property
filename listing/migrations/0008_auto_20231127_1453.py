# Generated by Django 3.1 on 2023-11-27 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_auto_20231118_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.IntegerField(primary_key=True),
        ),
    ]
