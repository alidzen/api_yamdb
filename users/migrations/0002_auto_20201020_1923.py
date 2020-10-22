# Generated by Django 3.0.5 on 2020-10-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='description',
            field=models.TextField(blank=True, help_text='Добавьте описание', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, help_text='Введите имя', max_length=150, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, help_text='Введите фамилию', max_length=150, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(blank=True, help_text='Введите имя пользователя', max_length=150, unique=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(help_text='Введите e-mail', max_length=255, unique=True, verbose_name='E-mail'),
        ),
    ]