# Generated by Django 3.0.5 on 2021-11-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juba', '0011_auto_20211119_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='unique_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
