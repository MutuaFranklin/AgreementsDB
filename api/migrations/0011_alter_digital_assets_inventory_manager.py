# Generated by Django 3.2.7 on 2021-12-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_digital_assets_inventory_web_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_assets_inventory',
            name='manager',
            field=models.CharField(max_length=255),
        ),
    ]
