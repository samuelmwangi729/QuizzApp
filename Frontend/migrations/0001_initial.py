# Generated by Django 4.2.11 on 2024-04-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('QuestionId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=500)),
                ('Option1', models.CharField(max_length=50)),
                ('Option2', models.CharField(max_length=50)),
                ('Option3', models.CharField(max_length=50)),
                ('CorrectAnswer', models.CharField(default='None', max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]