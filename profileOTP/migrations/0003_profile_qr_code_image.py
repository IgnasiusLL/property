# Generated by Django 3.1 on 2023-11-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileOTP', '0002_auto_20231129_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='qr_code_image',
            field=models.ImageField(null=True, upload_to='qrcodes/'),
        ),
    ]
