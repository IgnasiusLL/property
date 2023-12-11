# Generated by Django 3.1 on 2023-12-04 14:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0009_auto_20231127_1509'),
        ('realtors', '0011_auto_20231127_1509'),
        ('contacts', '0007_auto_20231203_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='apptDateTime',
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(default='Upcoming', max_length=100),
        ),
        migrations.CreateModel(
            name='ContactBackup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('status', models.CharField(default='Upcoming', max_length=100)),
                ('contact_date_start', models.DateTimeField(blank=True)),
                ('contact_date_end', models.DateTimeField(blank=True)),
                ('backup_date', models.DateTimeField(default=datetime.datetime.now)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.listing')),
                ('realtor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
