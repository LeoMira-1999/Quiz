# Generated by Django 3.2.5 on 2021-10-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0010_auto_20211022_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(),
        ),
    ]
