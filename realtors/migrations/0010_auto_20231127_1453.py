# Generated by Django 3.1 on 2023-11-27 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0009_remove_realtor_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='id',
            field=models.IntegerField(primary_key=True),
        ),
    ]
