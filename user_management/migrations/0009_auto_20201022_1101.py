# Generated by Django 3.1 on 2020-10-22 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_auto_20201022_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilebook',
            old_name='_status',
            new_name='status',
        ),
    ]