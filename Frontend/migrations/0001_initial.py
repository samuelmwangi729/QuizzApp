# Generated by Django 5.0.4 on 2024-05-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('QuestionId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=500)),
                ('Option1', models.TextField(max_length=500)),
                ('Option2', models.TextField(max_length=50)),
                ('Option3', models.TextField(max_length=500)),
                ('Option4', models.TextField(default=None, max_length=500)),
                ('Answered', models.BooleanField(default=False)),
                ('CorrectAnswer', models.TextField(default='None', max_length=500)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
