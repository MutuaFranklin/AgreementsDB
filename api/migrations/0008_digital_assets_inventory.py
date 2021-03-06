# Generated by Django 3.2.7 on 2021-12-01 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_profile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digital_assets_inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('platform_title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('managing_institution', models.CharField(max_length=255)),
                ('spatial_coverage', models.CharField(blank=True, max_length=255, null=True)),
                ('temporal_coverage', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True)),
                ('data_standards_compliance', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True)),
                ('web_services', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True)),
                ('license_type', models.CharField(blank=True, max_length=255, null=True)),
                ('backend_stack', models.CharField(blank=True, max_length=255, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='api.profile')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
