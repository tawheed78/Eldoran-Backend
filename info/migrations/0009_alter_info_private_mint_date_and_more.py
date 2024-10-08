# Generated by Django 4.2.4 on 2024-09-03 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_alter_info_private_mint_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='private_mint_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='info',
            name='private_mint_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='info',
            name='public_mint_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='info',
            name='public_mint_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
