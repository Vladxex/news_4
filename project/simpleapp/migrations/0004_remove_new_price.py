# Generated by Django 3.1.4 on 2021-01-19 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_new_auto_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='price',
        ),
    ]