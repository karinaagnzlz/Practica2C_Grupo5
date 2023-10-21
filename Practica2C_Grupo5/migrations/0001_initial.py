# Generated by Django 4.2.6 on 2023-10-17 06:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
            ],
        ),
    ]