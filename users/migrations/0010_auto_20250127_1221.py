# Generated by Django 3.2.25 on 2025-01-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190703_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='present',
            name='check_out_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='present',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
