# Generated by Django 5.0.2 on 2024-03-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='no_of_guest',
            new_name='no_of_guests',
        ),
    ]