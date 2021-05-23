# Generated by Django 3.1.7 on 2021-05-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_answer_question_test_testscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveSmallIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name': '[Test] Score',
                'verbose_name_plural': '[Test] Scores',
            },
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': '[Test] Answer', 'verbose_name_plural': '[Test] Answers'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '[Test] Question', 'verbose_name_plural': '[Test] Questions'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': '[Test] Test', 'verbose_name_plural': '[Test] Tests'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='questtion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='main.question'),
        ),
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.PositiveSmallIntegerField(help_text='Time duration for the Quiz in minutes'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(default='Test №', max_length=255),
        ),
        migrations.DeleteModel(
            name='TestScore',
        ),
        migrations.AddField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test'),
        ),
    ]