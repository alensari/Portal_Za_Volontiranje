# Generated by Django 3.2.7 on 2021-09-22 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oglasi', '0007_auto_20210919_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='datum_isteka_oglasa',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 20, 50, 23, 817224)),
        ),
    ]
