# Generated by Django 3.2.9 on 2021-12-03 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycourses', '0004_auto_20211203_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='end_till',
        ),
        migrations.RemoveField(
            model_name='team',
            name='start_at',
        ),
    ]