# Generated by Django 5.1.2 on 2025-02-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_remove_profile_email_notifications_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
