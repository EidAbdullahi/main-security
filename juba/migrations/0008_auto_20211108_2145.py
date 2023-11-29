# Generated by Django 3.0.5 on 2021-11-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juba', '0007_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='posted_by',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='posted_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
