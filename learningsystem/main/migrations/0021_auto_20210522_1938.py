# Generated by Django 3.1.7 on 2021-05-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210522_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testresult',
            options={'verbose_name': '[Test] Result', 'verbose_name_plural': '[Test] Results'},
        ),
        migrations.AddField(
            model_name='test',
            name='count_of_question_type_1',
            field=models.PositiveSmallIntegerField(default=0, help_text='Default type: 4 Answers'),
        ),
        migrations.AddField(
            model_name='test',
            name='count_of_question_type_2',
            field=models.PositiveSmallIntegerField(default=0, help_text='Extended type: N Answers (where n < k answers)'),
        ),
        migrations.AddField(
            model_name='test',
            name='count_of_question_type_3',
            field=models.PositiveSmallIntegerField(default=0, help_text='Input type: input your answer'),
        ),
    ]