# Generated by Django 2.2.5 on 2021-05-17 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20210517_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='ending_hours',
            new_name='working_hours',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='starting_hours',
            new_name='working_hours_end',
        ),
    ]
