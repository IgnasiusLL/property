# Generated by Django 3.1 on 2023-12-01 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerCmd', '0003_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='parent_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='customerCmd.reply'),
        ),
    ]
