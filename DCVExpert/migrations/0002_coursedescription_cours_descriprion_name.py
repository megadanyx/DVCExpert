# Generated by Django 5.1.7 on 2025-03-22 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCVExpert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedescription',
            name='cours_descriprion_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='DCVExpert.course'),
        ),
    ]
