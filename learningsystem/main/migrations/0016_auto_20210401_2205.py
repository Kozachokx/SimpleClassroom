# Generated by Django 3.1.7 on 2021-04-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210401_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='gay',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='small_pinus',
        ),
    ]
