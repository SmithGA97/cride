# Generated by Django 2.0.9 on 2021-10-01 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0002_auto_20210930_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='remaining_invitation',
            new_name='remaining_invitations',
        ),
    ]