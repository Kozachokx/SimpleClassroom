# Generated by Django 3.1.7 on 2021-04-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210401_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='practices',
            name='students',
            field=models.ManyToManyField(to='main.CustomUser'),
        ),
    ]
