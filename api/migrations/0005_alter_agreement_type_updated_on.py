# Generated by Django 3.2.7 on 2021-11-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_agreement_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement_type',
            name='updated_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]