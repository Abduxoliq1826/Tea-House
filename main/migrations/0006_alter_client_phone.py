# Generated by Django 4.1.1 on 2022-12-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_client_name_alter_order_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.BigIntegerField(unique=True),
        ),
    ]
