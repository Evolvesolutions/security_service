# Generated by Django 5.2 on 2025-05-02 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='created_at',
            new_name='submitted_at',
        ),
    ]
