# Generated by Django 2.2.5 on 2021-05-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20210509_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='working_hours',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='ending_hours',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='starting_hours',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
