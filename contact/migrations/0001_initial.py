# Generated by Django 4.0.4 on 2022-06-07 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('customer_need', models.CharField(max_length=200)),
                ('car_id', models.PositiveIntegerField()),
                ('car_title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.PositiveIntegerField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
