# Generated by Django 3.2.7 on 2021-12-03 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_digital_assets_inventory_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.role'),
        ),
    ]
