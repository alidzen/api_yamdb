# Generated by Django 3.0.5 on 2020-10-20 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20201020_1929'),
        ('users', '0004_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]