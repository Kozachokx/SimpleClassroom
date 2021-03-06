# Generated by Django 3.1.7 on 2021-04-01 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210401_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lection',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='practices',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='practices',
            name='students',
            field=models.ManyToManyField(to='main.Student'),
        ),
    ]
