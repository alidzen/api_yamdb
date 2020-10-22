# Generated by Django 3.0.5 on 2020-10-21 15:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20201021_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='confirmation_code',
            field=models.CharField(default=uuid.UUID('342f4e75-8517-4dae-8948-908d2a72a35e'), help_text='Input confirmation code', max_length=128, verbose_name='Confirmation Code'),
        ),
    ]