# Generated by Django 2.2.5 on 2021-05-09 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='restaurantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Restaurant Type',
            },
        ),
        migrations.CreateModel(
            name='WholeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Whole Menu',
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menuname_4',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menuname_5',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menuprice_4',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menuprice_5',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='facilities',
            field=models.ManyToManyField(to='restaurants.Facility'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.restaurantType'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='whole_menu',
            field=models.ManyToManyField(to='restaurants.WholeMenu'),
        ),
    ]
