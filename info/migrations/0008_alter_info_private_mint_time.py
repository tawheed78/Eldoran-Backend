# Generated by Django 4.2.4 on 2024-09-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_info_private_mint_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='private_mint_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
