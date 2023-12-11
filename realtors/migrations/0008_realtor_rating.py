# Generated by Django 3.1 on 2023-11-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_realtor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
