# Generated by Django 4.2.11 on 2024-04-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Answered',
            field=models.BooleanField(default=False),
        ),
    ]