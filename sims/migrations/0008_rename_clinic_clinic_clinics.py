# Generated by Django 4.2.3 on 2024-03-13 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sims', '0007_history_general_family_clinic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='Clinic',
            new_name='Clinics',
        ),
    ]
