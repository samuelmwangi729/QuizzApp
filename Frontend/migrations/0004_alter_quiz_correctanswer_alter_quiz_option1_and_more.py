# Generated by Django 4.2.11 on 2024-04-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0003_questionsanswers_quiz_option4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='CorrectAnswer',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='Option1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='Option3',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='Option4',
            field=models.CharField(default=None, max_length=500),
        ),
    ]