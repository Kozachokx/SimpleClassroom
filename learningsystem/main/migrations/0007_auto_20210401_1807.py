# Generated by Django 3.1.7 on 2021-04-01 15:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20210401_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DELETE', max_length=255)),
                ('body', models.TextField(blank=True, default='', max_length=255)),
                ('document', models.FileField(blank=True, default=None, null=True, upload_to='upload/')),
                ('open_time', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
        migrations.AlterField(
            model_name='lection',
            name='document',
            field=models.FileField(blank=True, default=None, null=True, upload_to='upload/'),
        ),
    ]
