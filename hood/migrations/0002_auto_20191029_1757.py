# Generated by Django 2.2.6 on 2019-10-29 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facilities',
            old_name='admin',
            new_name='author',
        ),
    ]
