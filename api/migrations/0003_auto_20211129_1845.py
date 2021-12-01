# Generated by Django 3.2.7 on 2021-11-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211129_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receiving_unep_division',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
