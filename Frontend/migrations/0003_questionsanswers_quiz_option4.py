# Generated by Django 4.2.11 on 2024-04-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_quiz_answered'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userrname', models.CharField(max_length=50)),
                ('rightQuestions', models.IntegerField(default=0)),
                ('wrongQuestions', models.IntegerField(default=0)),
                ('totalQuestions', models.IntegerField(default=0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='Option4',
            field=models.CharField(default=None, max_length=50),
        ),
    ]