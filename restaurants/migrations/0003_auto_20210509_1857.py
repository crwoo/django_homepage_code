# Generated by Django 2.2.5 on 2021-05-09 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20210509_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='restaurants.Facility'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='whole_menu',
            field=models.ManyToManyField(blank=True, to='restaurants.WholeMenu'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
