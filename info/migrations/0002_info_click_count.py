# Generated by Django 4.2.4 on 2024-09-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='click_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
