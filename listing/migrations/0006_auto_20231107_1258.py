# Generated by Django 3.1 on 2023-11-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_auto_20231107_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default='/image/noIMG.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
